# By XWcode-fre    yaaaay
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QWidget, QTabWidget, QToolBar, QAction
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

#Adding Class
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FreakBrowser")
        self.setGeometry(100, 100, 1280, 720)

        # Browser Tab
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)
        self.setCentralWidget(self.tabs)

        # Creating new tab
        self.add_tab("https://www.google.com")

        # Tool bar
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # Url Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Type utl here")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)

        #Navigateion
        self.add_toolbar_button("←", self.navigate_back)
        self.add_toolbar_button("→", self.navigate_forward)
        self.add_toolbar_button("⟳", self.reload_page)
        self.add_toolbar_button("🏠", self.navigate_home)

        #New Tab Button
        self.add_toolbar_button("+", self.add_tab)

    def add_toolbar_button(self, text, callback):
        """Toolbar Button."""
        action = QAction(text, self)
        action.triggered.connect(callback)
        self.toolbar.addAction(action)

    def add_tab(self, url=None):
        """Creating new tab"""
        browser = QWebEngineView()
        browser.setUrl(QUrl(url) if url else QUrl("https://www.google.com"))
        browser.urlChanged.connect(self.update_url_bar)

        # Adding new tab
        i = self.tabs.addTab(browser, "Новая вкладка")
        self.tabs.setCurrentIndex(i)

    def close_tab(self, index):
        """Closing tab"""
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()  # Closing app when last tab is closed

    def navigate_to_url(self):
        """Going to url"""
        url = self.url_bar.text()
        if not url.startswith("http") and "." not in url:
            #If url is not valid
            url = f"https://www.google.com/search?q={url}"
        elif not url.startswith("http"):
            # If url in tab add http://"
            url = "http://" + url

        current_browser = self.tabs.currentWidget()
        current_browser.setUrl(QUrl(url))

    def update_url_bar(self, url=None):
        """Adding addres."""
        if url is None:
            current_browser = self.tabs.currentWidget()
            if current_browser:
                url = current_browser.url()
        if url and isinstance(url, QUrl):
            self.url_bar.setText(url.toString())

    def navigate_back(self):
        """Navigation back."""
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.back()

    def navigate_forward(self):
        """Navigation forward."""
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.forward()

    def reload_page(self):
        """Reloading page."""
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.reload()

    def navigate_home(self):
        """ Navigation home."""
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.setUrl(QUrl("https://www.google.com"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

 
    browser = Browser()
    browser.show()

    sys.exit(app.exec_())
    #Thank you for downloading my code❤️❤️
