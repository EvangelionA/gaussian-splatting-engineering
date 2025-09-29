#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3DGS GUI 训练控制器
"""

import os
import sys
import time
import re
import subprocess
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QProcess
from PyQt5.QtWidgets import QApplication

class TrainingController(QObject):
    """训练控制器，负责与train.py交互"""
    
    # 信号定义
    output_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(dict)
    finished_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.process = None
        self.start_time = None
        self.total_iterations = 0
        self.current_iteration = 0
    
    def start_training(self, config):
        """启动训练进程"""
        if self.process is not None and self.process.state() == QProcess.Running:
            self.output_signal.emit("已有训练进程在运行，请先停止当前进程。")
            return
        
        # 记录开始时间和总迭代次数
        self.start_time = time.time()
        self.total_iterations = config['iterations']
        self.current_iteration = 0
        
        # 创建进程
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        
        # 连接信号
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.finished.connect(self.process_finished)
        
        # 构建命令行参数
        args = self.build_command_args(config)
        
        # 启动进程
        self.output_signal.emit("启动训练进程...")
        self.output_signal.emit(f"命令: python gaussian-splatting-main/train.py {' '.join(args)}")
        
        # 设置工作目录为项目根目录
        self.process.setWorkingDirectory(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # 启动进程
        self.process.start("python", ["gaussian-splatting-main/train.py"] + args)
    
    def build_command_args(self, config):
        """构建命令行参数"""
        args = []
        
        # 基本参数
        args.append(f"--source_path={config['source_path']}")
        args.append(f"--model_path={config['model_path']}")
        args.append(f"--iterations={config['iterations']}")
        
        # 默认模型参数
        args.append(f"--sh_degree={config['sh_degree']}")
        
        # 训练控制
        args.append(f"--densify_from_iter={config['densify_from_iter']}")
        args.append(f"--densify_until_iter={config['densify_until_iter']}")
        args.append(f"--densification_interval={config['densification_interval']}")
        
        # 测试和保存迭代
        args.append("--test_iterations")
        for iter_num in config['test_iterations']:
            args.append(str(iter_num))
        
        args.append("--save_iterations")
        for iter_num in config['save_iterations']:
            args.append(str(iter_num))
        
        return args
    
    def handle_output(self):
        """处理进程输出"""
        if self.process is None:
            return
        
        # 读取输出
        output = self.process.readAllStandardOutput().data().decode('utf-8', errors='replace')
        self.output_signal.emit(output)
        
        # 解析进度信息
        self.parse_progress(output)
    
    def parse_progress(self, output):
        """解析输出中的进度信息"""
        # 解析迭代次数
        iter_match = re.search(r'(\d+)/(\d+)', output)
        if iter_match:
            self.current_iteration = int(iter_match.group(1))
            
            # 计算剩余时间
            if self.start_time is not None and self.current_iteration > 0:
                elapsed = time.time() - self.start_time
                iterations_per_second = self.current_iteration / elapsed
                remaining_iterations = self.total_iterations - self.current_iteration
                
                if iterations_per_second > 0:
                    remaining_seconds = remaining_iterations / iterations_per_second
                    remaining_time = self.format_time(remaining_seconds)
                else:
                    remaining_time = "计算中..."
            else:
                remaining_time = "计算中..."
            
            # 解析损失值
            loss_match = re.search(r'Loss: ([\d\.]+)', output)
            loss = loss_match.group(1) if loss_match else "N/A"
            
            # 发送进度信号
            self.progress_signal.emit({
                'iteration': self.current_iteration,
                'total_iterations': self.total_iterations,
                'loss': loss,
                'remaining_time': remaining_time
            })
    
    def format_time(self, seconds):
        """格式化时间"""
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if hours > 0:
            return f"{hours}小时 {minutes}分钟"
        elif minutes > 0:
            return f"{minutes}分钟 {seconds}秒"
        else:
            return f"{seconds}秒"
    
    def stop_training(self):
        """停止训练进程"""
        if self.process is not None and self.process.state() == QProcess.Running:
            self.process.kill()
            self.output_signal.emit("训练进程已终止。")
    
    def process_finished(self, exit_code, exit_status):
        """进程结束处理"""
        if exit_code == 0:
            self.output_signal.emit("训练完成，退出代码: 0")
        else:
            self.output_signal.emit(f"训练异常终止，退出代码: {exit_code}")
        
        self.finished_signal.emit()
        self.process = None