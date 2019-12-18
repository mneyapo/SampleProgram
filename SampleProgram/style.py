#         self.LIB_L4.setStyleSheet(
#                 """QLabel {font-family:"Courier New", Courier, monospace ; font-size: 20px; }""")

#         font = self.line.font()      # lineedit current font
#         font.setPointSize(32)               # change it's size
#         self.line.setFont(font)      # set font
#         self.line.setFixedWidth(32)

# Layout
#         self.lay = QHBoxLayout()
#         self.setLayout(self.lay)
#         self.btn_OK.clicked.connect(lambda: self.pressedOnButton())
# set image
#         self.LIB_L2.setPixmap(pixmap)
#         self.LIB_L2.resize(pixmap.width(),pixmap.height())
#         self.line.setValidator(QIntValidator(0,1000))
#         self.nameLabel.setText('Name:')

#         QLineEdit readonly
#         self.ui.lineEdit_4.setReadOnly(True)
#         self.LIB_L1.setStyleSheet("background-color: rgb(0,63,128);") #change QLineEdit background color
#         self.LIB_L1.setStyleSheet("color: yellow;")
#         original saved stysheet
#         ss= le.styleSheet()
#         le.setStyleSheet(ss)# back to original

#self.ui.label.setFont(QtGui.QFont('SansSerif', 30)) # change