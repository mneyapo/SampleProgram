# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys
import json
import time
import datetime as DT
import threading
from threading import Thread
# This gets the Qt stuff
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *     # (QApplication, QCalendarWidget, QCheckBox,QComboBox, QDateEdit, QGridLayout, QGroupBox, QHBoxLayout, QLabel,QLayout, QWidget)
from PyQt5.QtGui import  *        # QFont, QTextCharFormat
from PyQt5 import QtCore,QtGui,QtNetwork
#from PyQt5.QtGui import QKeyEvent

# This is our window from QtCreator
import mainwindow_auto

starttime=time.time()
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call     
    def clickMethod(self):
        # Retrieves text in the field
        sQR = self.line.text().upper()
        self.LIB_BADGE.setText(sQR)
        print('QR Code: ' + self.line.text().upper())
        self.LIB_L3.setText(sQR)
        self.LIB_L4.setText("VEUILLEZ PATIENTER...")
        self.LIB_BADGE.setText(sQR)
        # Erases the contents of line Text
        self.line.clear()
       
      
    def textChangedMethod(self):
        pass
        #print (self.line.size())
#         print (self.line.height())
#         print (self.line.geometry().height())
#         print (self.line.frameGeometry().height())
#       
#         print (self.line.frameSize().height())
#         print (self.line.rect())
        #print ("As text in the box changes",self.line.text())
        
    def doRequest(self):
        print("Do request")
#         url = "http://fifm2019-rest.e-maroc.org/FIFM_2019/HELLO_L/SDC-XX"
#         req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
# 
#         self.nam = QtNetwork.QNetworkAccessManager()
#         self.nam.finished.connect(self.handleResponse)
#         self.nam.get(req)    

    def handleResponse(self, reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()
            json_ar = json.loads(str(bytes_string, 'utf-8'))
            print(str(bytes_string, 'utf-8'))
            data = json_ar
            print('Message: {0}'.format(data['Message']))
            print('L1: {0}'.format(data['L1']))
            print('L2: {0}'.format(data['L2']))
            self.LIB_L1.setText(data['L1'])
            self.LIB_L2.setText(data['L2'])
        else:
            print("Error occured: ", er)
            print(reply.errorString())

            QtCore.QCoreApplication.quit()    

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        #self.processEvents()
        
#         self.checkThreadTimer = QtCore.QTimer(self)
#         self.checkThreadTimer.setInterval(500) #.5 seconds
#         self.checkThreadTimer.timeout.connect(self.readListValues)
        # NumField 
        self.line.setPlaceholderText("Scan QR code")
        self.line.setStyleSheet("""QLineEdit { background-color: white; color: black }""")
        
        # Sets the validation rules.
        """ Available validators

            QIntValidator − Restricts input to integer

            QDoubleValidator − Fraction part of number limited to specified decimals

            QRegexpValidator − Checks input against a Regex expression
        """
        
        #self.line.setValidator(QIntValidator())
        # Field limits
        
        # Sets the maximum number of characters for input
        self.line.setMaxLength(30)
        # set Alignment (Qt.AlignLeft, Qt.AlignRight , Qt.AlignCenter , Qt.AlignJustify, Qt.AlignTop)
        self.line.setAlignment(Qt.AlignLeft)
        # Displays the contents QFont object
        self.line.setFont(QFont("Arial",20))
        
        # set StyleSheet Label background-color , color and border
        self.LIB_L1.setStyleSheet("""QLabel { background-color: blue; color: yellow }""")
        self.LIB_L2.setStyleSheet("""QLabel { background-color: blue; color: yellow }""")
        self.LIB_L3.setStyleSheet("""QLabel { border: 1px solid orange; background-color: yellow; color: blue }""")
        self.LIB_L4.setStyleSheet("""QLabel { border: 1px solid orange; color: blue }""")
        self.LIB_BADGE.setStyleSheet("""QLabel { border: 1px solid red; color: blue }""")
        # change Label font type and size 
        self.LIB_L1.setFont(QFont('Courier New', 20)) 
        self.LIB_L2.setFont(QFont('Courier New', 20)) # change font type and size
        self.LIB_L3.setFont(QFont('Courier New', 20)) # change font type and size
        self.LIB_L4.setFont(QFont('Courier New', 20)) # change font type and size
        # Text Color

        # Programmatically sets the text
        self.LIB_L1.setText('L1')
        self.LIB_L2.setText('L2')
        self.LIB_L3.setText('PASSER VOTRE BADGE OU INVITATION')
        self.LIB_L4.setText('L4')
        
        # When you press ‘Enter’
        self.line.returnPressed.connect(self.clickMethod)
        

        """ As text in the box changes either by input or by programmatic means"""
        self.line.textChanged.connect(self.textChangedMethod)
        
        self.__timer_init = QtCore.QTimer()
        self.__timer_init.timeout.connect( self.__completeInit )
        self.__timer_init.setSingleShot( True )
        self.__timer_init.start( 0 )
        
        self._status_update_timer = QTimer(self)
        self._status_update_timer.setSingleShot(False)
        self._status_update_timer.setInterval(60000)
        self._status_update_timer.timeout.connect(self._update_status)
        self._status_update_timer.start()
        #self._status_update_timer.start(60000)
        
        self.LIB_BADGE.setAlignment(Qt.AlignCenter)
        
        pixmap=QPixmap('VST01341_16_1.png')
        self.LIB_COMBO_IMG.setPixmap(pixmap)
        self.LIB_COMBO_IMG.resize(pixmap.width(),pixmap.height())

        #self.doRequest()
    def keyPressEvent(self, e):
        #  pressedkey = e.key()
        # pressedkey == Qt.Key_Enter or pressedkey == Qt.Key_Return:
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key == Qt.Key_Enter  or e.key == Qt.Key_Return:
            self.clickMethod()
    
    def _update_status(self):
        startTime = time.time()
        self.doRequest()
        print("Updated",starttime)
        
    def __completeInit( self ):
        self.__timer_init = None
        self.completeInit()

    def completeInit( self ):
        self.is_running = True
        self.doRequest()
        starttime=time.time()
        print("Updated",starttime)
            
# I feel better having one of these
def main():
    rpiname = "SDC-XX"
    url_WS_HELLO_L="http://fifm2019-rest.e-maroc.org/FIFM_2019/HELLO_L/"+rpiname
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    QApplication.processEvents()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
    #  app.exec_() 

# python bit to figure how who started This
if __name__ == "__main__":
    main()