#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3DGS GUI 工具函数
"""

import os
import sys
import re
import time
from datetime import datetime

def get_project_root():
    """获取项目根目录"""
    # 假设当前文件在gui文件夹下
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def format_time_delta(seconds):
    """将秒数格式化为可读的时间差"""
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours > 0:
        return f"{hours}小时 {minutes}分钟 {seconds}秒"
    elif minutes > 0:
        return f"{minutes}分钟 {seconds}秒"
    else:
        return f"{seconds}秒"

def get_timestamp():
    """获取当前时间戳，格式为YYYYMMDD_HHMMSS"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def ensure_dir(directory):
    """确保目录存在，如果不存在则创建"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def parse_iterations_string(iterations_str):
    """解析迭代次数字符串，返回整数列表"""
    try:
        return [int(x.strip()) for x in iterations_str.split(',') if x.strip()]
    except ValueError:
        return []

def get_available_datasets(base_dir=None):
    """获取可用的数据集列表"""
    if base_dir is None:
        base_dir = os.path.join(get_project_root(), "data")
    
    if not os.path.exists(base_dir):
        return []
    
    # 查找包含images文件夹的目录
    datasets = []
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "images")):
            datasets.append(item)
    
    return datasets

def get_output_directories(base_dir=None):
    """获取输出目录列表"""
    if base_dir is None:
        base_dir = os.path.join(get_project_root(), "output")
    
    if not os.path.exists(base_dir):
        return []
    
    # 查找输出目录
    outputs = []
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            outputs.append(item)
    
    return outputs

def parse_log_file(log_path):
    """解析日志文件，提取关键信息"""
    if not os.path.exists(log_path):
        return {}
    
    info = {
        'iterations': [],
        'loss': [],
        'psnr': [],
        'timestamps': []
    }
    
    try:
        with open(log_path, 'r') as f:
            content = f.read()
            
            # 提取迭代信息
            iter_matches = re.findall(r'\[ITER (\d+)\]', content)
            info['iterations'] = [int(i) for i in iter_matches]
            
            # 提取PSNR信息
            psnr_matches = re.findall(r'PSNR ([\d\.]+)', content)
            info['psnr'] = [float(p) for p in psnr_matches]
            
            # 提取Loss信息
            loss_matches = re.findall(r'L1 ([\d\.]+)', content)
            info['loss'] = [float(l) for l in loss_matches]
            
            # 提取时间戳
            time_matches = re.findall(r'\[([\d/]+ [\d:]+)\]', content)
            info['timestamps'] = time_matches
    except Exception as e:
        print(f"解析日志文件出错: {e}")
    
    return info