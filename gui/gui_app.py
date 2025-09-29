#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3DGS GUI 主应用程序
"""

import os
import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QPushButton, QLabel, QFileDialog, QTabWidget,
                            QTextEdit, QProgressBar, QMessageBox, QSplitter,
                            QGroupBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QIcon

from config_panel import ConfigPanel
from train_controller import TrainingController

class GaussianSplattingGUI(QMainWindow):
    """3D高斯散射训练GUI主窗口"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gaussian-splatting-engineering-gui")
        self.resize(1024, 512)
        
        # 设置最小窗口尺寸，防止UI元素被遮挡
        self.setMinimumSize(800, 500)
        
        # 设置应用图标
        icon_path = os.path.join(os.path.dirname(__file__), "assert", "gaussian-splatting.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # 初始化UI组件
        self.init_ui()
        
        # 初始化训练控制器
        self.training_controller = TrainingController()
        self.training_controller.output_signal.connect(self.update_output)
        self.training_controller.progress_signal.connect(self.update_progress)
        self.training_controller.finished_signal.connect(self.training_finished)
        
        # 状态变量
        self.is_training = False
        
    def init_ui(self):
        """初始化UI界面"""
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 创建分割器，允许用户调整上下两部分的大小
        splitter = QSplitter(Qt.Vertical)
        main_layout.addWidget(splitter)
        
        # 上半部分 - 配置面板
        top_widget = QWidget()
        top_layout = QVBoxLayout(top_widget)
        
        
        # 数据集选择部分
        dataset_layout = QHBoxLayout()
        
        self.dataset_label = QLabel("数据集路径:")
        self.dataset_path = QLabel("未选择")
        self.browse_button = QPushButton("浏览...")
        self.browse_button.clicked.connect(self.browse_dataset)
        
        dataset_layout.addWidget(self.dataset_label)
        dataset_layout.addWidget(self.dataset_path, 1)
        dataset_layout.addWidget(self.browse_button)
        
        top_layout.addLayout(dataset_layout)
        
        # 配置面板 - 只保留基本参数
        self.config_panel = ConfigPanel()
        top_layout.addWidget(self.config_panel)
        
        # 控制按钮 (添加到配置面板的布局中)
        control_layout = QHBoxLayout()
        self.start_button = QPushButton("开始训练")
        self.start_button.clicked.connect(self.start_training)
        self.stop_button = QPushButton("停止训练")
        self.stop_button.clicked.connect(self.stop_training)
        self.stop_button.setEnabled(False)
        
        control_layout.addWidget(self.start_button)
        control_layout.addWidget(self.stop_button)
        
        # 获取基本参数组的布局并添加控制按钮
        basic_group = self.config_panel.findChild(QGroupBox)
        if basic_group:
            basic_group.layout().addRow(control_layout)
        
        # 添加到分割器
        splitter.addWidget(top_widget)
        
        # 下半部分 - 输出和进度
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout(bottom_widget)
        
        # 进度区域 (放在顶部)
        progress_group = QGroupBox("训练进度")
        progress_layout = QVBoxLayout(progress_group)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        # 进度信息 (水平排列)
        progress_info_layout = QHBoxLayout()
        self.iteration_label = QLabel("迭代: 0 / 0")
        self.loss_label = QLabel("损失: N/A")
        self.time_label = QLabel("预计剩余时间: N/A")
        
        progress_info_layout.addWidget(self.iteration_label)
        progress_info_layout.addWidget(self.loss_label)
        progress_info_layout.addWidget(self.time_label)
        
        progress_layout.addWidget(self.progress_bar)
        progress_layout.addLayout(progress_info_layout)
        bottom_layout.addWidget(progress_group)
        
        # 日志区域 (放在底部)
        log_group = QGroupBox("训练日志")
        log_layout = QVBoxLayout(log_group)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Courier New", 10))
        log_layout.addWidget(self.output_text)
        bottom_layout.addWidget(log_group)
        
        # 设置布局比例 (进度区域占1/3，日志区域占2/3)
        bottom_layout.setStretch(0, 1)
        bottom_layout.setStretch(1, 2)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
       
        
        # 添加到分割器
        splitter.addWidget(bottom_widget)
        
        # 设置初始分割比例
        splitter.setSizes([400, 300])
    
    def browse_dataset(self):
        """浏览并选择数据集文件夹"""
        folder = QFileDialog.getExistingDirectory(self, "选择数据集文件夹")
        if folder:
            self.dataset_path.setText(folder)
    
    def start_training(self):
        """开始训练过程"""
        # 检查数据集路径
        dataset_path = self.dataset_path.text()
        if dataset_path == "未选择":
            QMessageBox.warning(self, "警告", "请先选择数据集路径!")
            return
        
        # 获取配置参数
        config = self.config_panel.get_config()
        config['source_path'] = dataset_path
        
        # 更新UI状态
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.is_training = True
        
        # 清空输出
        self.output_text.clear()
        self.progress_bar.setValue(0)
        self.iteration_label.setText(f"迭代: 0 / {config['iterations']}")
        self.loss_label.setText("损失: N/A")
        self.time_label.setText("预计剩余时间: N/A")
        
        # 切换到输出标签页
        self.tabs.setCurrentIndex(0)
        
        # 开始训练
        self.training_controller.start_training(config)
    
    def stop_training(self):
        """停止训练过程"""
        reply = QMessageBox.question(self, '确认', 
                                    '确定要停止训练吗？当前进度将会丢失。',
                                    QMessageBox.Yes | QMessageBox.No, 
                                    QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.training_controller.stop_training()
            self.update_output("训练已手动停止。")
            self.training_finished()
    
    def update_output(self, text):
        """更新输出文本"""
        self.output_text.append(text)
        # 滚动到底部
        self.output_text.verticalScrollBar().setValue(
            self.output_text.verticalScrollBar().maximum()
        )
    
    def update_progress(self, progress_data):
        """更新进度信息"""
        iteration = progress_data.get('iteration', 0)
        total_iterations = progress_data.get('total_iterations', 100)
        loss = progress_data.get('loss', 'N/A')
        remaining_time = progress_data.get('remaining_time', 'N/A')
        
        # 更新进度条
        progress = int((iteration / total_iterations) * 100) if total_iterations > 0 else 0
        self.progress_bar.setValue(progress)
        
        # 更新标签
        self.iteration_label.setText(f"迭代: {iteration} / {total_iterations}")
        self.loss_label.setText(f"损失: {loss}")
        self.time_label.setText(f"预计剩余时间: {remaining_time}")
    
    def training_finished(self):
        """训练完成后的处理"""
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.is_training = False
        
        # 显示完成消息
        self.update_output("\n训练完成!")
        
        # 切换到进度标签页以显示最终结果
        self.tabs.setCurrentIndex(1)
    
    def closeEvent(self, event):
        """窗口关闭事件处理"""
        if self.is_training:
            reply = QMessageBox.question(self, '确认', 
                                        '训练正在进行中，确定要退出吗？',
                                        QMessageBox.Yes | QMessageBox.No, 
                                        QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                self.training_controller.stop_training()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()