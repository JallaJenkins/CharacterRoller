import sys
import time
from random import randint, seed
from functools import partial

from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget,
    QLabel, QToolBar, QAction, QStatusBar, QDockWidget, QMenuBar, QMenu, QLineEdit, QPushButton,
    QStackedLayout, QVBoxLayout,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

from abilities import *
from character import *
from personal_info import *
from details import *


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        character = Character()
        self.setWindowTitle("Character Roller")
        self.setMinimumSize(QSize(1024, 768))

        self.abilities_dock = AbilitiesDock(character)
        self.abilities_dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.abilities_dock, Qt.Vertical)

        self.personal_info_dock = PersonalInfoDock(character)
        self.personal_info_dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.addDockWidget(Qt.TopDockWidgetArea, self.personal_info_dock, Qt.Horizontal)

        self.centre = DetailsTabs(character)
        self.setCentralWidget(self.centre)


app = QApplication(sys.argv)
app.setStyle('Fusion')
w = MainWindow()
w.show()

app.exec()
