#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3DGS GUI 入口点
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from gui_app import GaussianSplattingGUI

def main():
    """主函数，启动GUI应用"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 使用Fusion风格，在所有平台上看起来都比较一致
    
    # 确保当前工作目录正确
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.dirname(script_dir))  # 切换到项目根目录
    
    window = GaussianSplattingGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()