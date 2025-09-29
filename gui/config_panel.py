#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3DGS GUI 配置面板
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
                            QLabel, QLineEdit, QComboBox, QCheckBox, 
                            QSpinBox, QDoubleSpinBox, QGroupBox, QScrollArea,
                            QPushButton, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
import subprocess
from PyQt5.QtCore import Qt

class ConfigPanel(QWidget):
    """训练参数配置面板"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """初始化UI界面"""
        # 创建滚动区域以容纳所有配置选项
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        
        # 创建内容窗口
        content = QWidget()
        scroll_layout = QVBoxLayout(content)
        
        # 添加配置组 - 只保留基本参数
        scroll_layout.addWidget(self.create_basic_group())
        
        # 设置滚动区域的窗口部件
        scroll.setWidget(content)
        
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll)
    
    def create_basic_group(self):
        """创建基本参数组"""
        group = QGroupBox()
        layout = QFormLayout()
        
        # 输出路径
        output_layout = QHBoxLayout()
        self.model_path = QLineEdit("./output")
        self.model_path.setToolTip("模型输出路径")
        self.browse_output_button = QPushButton("浏览...")
        self.browse_output_button.clicked.connect(self.browse_output_path)
        
        output_layout.addWidget(self.model_path)
        output_layout.addWidget(self.browse_output_button)
        layout.addRow("输出路径:", output_layout)
        
        # 迭代次数
        self.iterations = QSpinBox()
        self.iterations.setRange(1000, 100000)
        self.iterations.setValue(30000)
        self.iterations.setSingleStep(1000)
        self.iterations.setToolTip("训练的总迭代次数")
        layout.addRow("迭代次数:", self.iterations)
        
        # Viewer路径
        viewer_layout = QHBoxLayout()
        self.viewer_path = QLineEdit()
        self.viewer_path.setToolTip("3DGS查看器路径")
        self.browse_viewer_button = QPushButton("浏览...")
        self.browse_viewer_button.clicked.connect(self.browse_viewer_path)
        
        viewer_layout.addWidget(self.viewer_path)
        viewer_layout.addWidget(self.browse_viewer_button)
        layout.addRow("3DGS查看器:", viewer_layout)
        
        # 模型文件夹
        model_folder_layout = QHBoxLayout()
        self.model_folder_path = QLineEdit()
        self.model_folder_path.setToolTip("3DGS模型文件夹路径")
        self.browse_model_folder_button = QPushButton("浏览...")
        self.browse_model_folder_button.clicked.connect(self.browse_model_folder_path)
        
        model_folder_layout.addWidget(self.model_folder_path)
        model_folder_layout.addWidget(self.browse_model_folder_button)
        layout.addRow("模型文件夹:", model_folder_layout)
        
        # 显示模型按钮
        self.show_model_button = QPushButton("显示3DGS模型")
        self.show_model_button.clicked.connect(self.show_model)
        layout.addRow(self.show_model_button)
        
        group.setLayout(layout)
        return group
    
    def create_training_group(self):
        """创建训练控制参数组"""
        group = QGroupBox("训练控制")
        layout = QFormLayout()
        
        # 密度控制参数
        self.densify_from_iter = QSpinBox()
        self.densify_from_iter.setRange(0, 10000)
        self.densify_from_iter.setValue(500)
        self.densify_from_iter.setToolTip("开始密度控制的迭代次数")
        layout.addRow("密度控制开始迭代:", self.densify_from_iter)
        
        self.densify_until_iter = QSpinBox()
        self.densify_until_iter.setRange(1000, 100000)
        self.densify_until_iter.setValue(15000)
        self.densify_until_iter.setToolTip("结束密度控制的迭代次数")
        layout.addRow("密度控制结束迭代:", self.densify_until_iter)
        
        self.densification_interval = QSpinBox()
        self.densification_interval.setRange(10, 1000)
        self.densification_interval.setValue(100)
        self.densification_interval.setToolTip("密度控制的间隔")
        layout.addRow("密度控制间隔:", self.densification_interval)
        
        # 测试迭代
        self.test_iterations = QLineEdit("7000, 30000")
        self.test_iterations.setToolTip("测试迭代次数，用逗号分隔")
        layout.addRow("测试迭代:", self.test_iterations)
        
        # 保存迭代
        self.save_iterations = QLineEdit("7000, 30000")
        self.save_iterations.setToolTip("保存模型的迭代次数，用逗号分隔")
        layout.addRow("保存迭代:", self.save_iterations)
        
        group.setLayout(layout)
        return group
    
    def browse_output_path(self):
        """浏览并选择输出路径"""
        folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹")
        if folder:
            self.model_path.setText(folder)
    
    def browse_viewer_path(self):
        """浏览并选择viewer.exe路径"""
        file, _ = QFileDialog.getOpenFileName(self, "选择3DGS查看器", "", "Executable Files (*.exe)")
        if file:
            self.viewer_path.setText(file)
    
    def browse_model_folder_path(self):
        """浏览并选择模型文件夹路径"""
        folder = QFileDialog.getExistingDirectory(self, "选择模型文件夹")
        if folder:
            self.model_folder_path.setText(folder)
    
    def show_model(self):
        """显示3DGS模型"""
        viewer = self.viewer_path.text()
        model_folder = self.model_folder_path.text()
        
        if not viewer:
            QMessageBox.warning(self, "警告", "请先选择3DGS查看器路径!")
            return
        if not model_folder:
            QMessageBox.warning(self, "警告", "请先选择模型文件夹路径!")
            return
            
        try:
            subprocess.Popen([viewer, "--m", model_folder])
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法启动查看器: {str(e)}")
    
    def get_config(self):
        """获取当前配置参数"""
        config = {
            # 基本参数
            'model_path': self.model_path.text(),
            'iterations': self.iterations.value(),
            
            # Viewer和模型路径
            'viewer_path': self.viewer_path.text(),
            'model_folder_path': self.model_folder_path.text(),
            
            # 默认模型参数
            'sh_degree': 3,
            
            # 默认优化参数
            'optimizer_type': 'default',
            'position_lr_init': 0.00016,
            'position_lr_final': 0.0000016,
            'feature_lr': 0.0025,
            'opacity_lr': 0.05,
            'scaling_lr': 0.005,
            'rotation_lr': 0.001,
            'lambda_dssim': 0.2,
            
            # 默认管道参数
            'convert_SHs_python': False,
            'compute_cov3D_python': False,
            
            # 默认训练控制参数
            'densify_from_iter': 500,
            'densify_until_iter': 15000,
            'densification_interval': 100,
            'test_iterations': [7000, 30000],
            'save_iterations': [7000, 30000],
        }
        """获取当前配置参数"""
        config = {
            # 基本参数
            'model_path': self.model_path.text(),
            'iterations': self.iterations.value(),
            
            # 默认模型参数
            'sh_degree': 3,
            
            # 默认优化参数
            'optimizer_type': 'default',
            'position_lr_init': 0.00016,
            'position_lr_final': 0.0000016,
            'feature_lr': 0.0025,
            'opacity_lr': 0.05,
            'scaling_lr': 0.005,
            'rotation_lr': 0.001,
            'lambda_dssim': 0.2,
            
            # 默认管道参数
            'convert_SHs_python': False,
            'compute_cov3D_python': False,
            
            # 默认训练控制参数
            'densify_from_iter': 500,
            'densify_until_iter': 15000,
            'densification_interval': 100,
            'test_iterations': [7000, 30000],
            'save_iterations': [7000, 30000],
        }
        
        return config