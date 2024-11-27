#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/6/29 9:12   xxx      1.0         None
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from chipthermal.ui.form import Form
import chipthermal.img_rc
import ctypes
# 任务栏显示图标，仅限于windows
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ims-chip-thermal")


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__()
        self.resize(850, 400)
        self.setWindowTitle('微系统热阻分析法计算器')

        self.setWindowIcon(QPixmap(':/img/image/icon.ico'))
        self.form = Form(self)
        self.setCentralWidget(self.form)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
