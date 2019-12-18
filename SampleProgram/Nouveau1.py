from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
import sys

def printContent():
 answerAsText = bytes(replyObject.readAll()).decode("utf-8")
 print(answerAsText)


class mainClass():
 def my_exception_hook(exctype, value, traceback):

     print(exctype, value, traceback)

     sys._excepthook(exctype, value, traceback)
     sys.exit(1)

 sys.excepthook = my_exception_hook


if __name__ == '__main__':
 app = QApplication(sys.argv)

 url = QUrl("http://www.google.com")

 request = QNetworkRequest()
 request.setUrl(url)
 manager = QNetworkAccessManager()

 replyObject = manager.get(request)
 replyObject.finished.connect(printContent)

 sys.exit(app.exec_())

