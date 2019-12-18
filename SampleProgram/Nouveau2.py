self.lineEdit1 = QtGui.QLineEdit(self)    #URL
self.lineEdit2 = QtGui.QLineEdit(self)    # API KEY
self.pushButton = QtGui.QPushButton(self)   # SEND BUTTON
QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.doIt)

def doIt(self):
    parameters = {"url": str(self.lineEdit1.text()),"apikey": str(self.lineEdit2.text())}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    print json