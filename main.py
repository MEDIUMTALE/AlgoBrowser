# -*- coding: UTF-8 -*-

# Algo Browser
# project version 1.5

# Задачи:

# 1. Починить вход в онлайн уроки. ✔
# 2. Добавить URL строку. ✔
# 3. Функционал обычного браузера. ✔
# 4. Сделать вкладки. ✖


# import`s
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

# MainWindow class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl("https://learn.algoritmika.org/login"))

        self.browser.urlChanged.connect(self.update_urlbar)

        self.browser.loadFinished.connect(self.update_title)

        self.setCentralWidget(self.browser)

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")

        self.addToolBar(navtb)

        back_btn = QAction("←", self)


        back_btn.triggered.connect(self.browser.back)

        navtb.addAction(back_btn)

        next_btn = QAction("→", self)

        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("↻", self)

        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("🏠", self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        navtb.addSeparator()
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)
        stop_btn = QAction("✖", self)
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Algo Browser" % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())

        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())

        self.urlbar.setCursorPosition(0)


# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Algo Browser")
app.setWindowIcon(QIcon('web.png'))

# creating a main window object
window = MainWindow()

# exit
app.exec_()