from PyQt5 import QtCore, QtGui, QtWidgets

class news_ui(QtWidgets.QListWidget):
    def __init__(self, *args, **kwargs):
        super(news_ui, self).__init__(*args, **kwargs)
        self.setGeometry(QtCore.QRect(240, 110, 520, 450))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWordWrap(True)
        self.setSpacing(2)

    #def add_News()