from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from pandas.plotting import register_matplotlib_converters
import webbrowser
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

register_matplotlib_converters()
data = mysql.connector.connect(
    host="myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com",
    user="myrds",
    passwd="admin123",
    database="myrds1"
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 616)
        MainWindow.setToolTipDuration(0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chartsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.chartsView.setGeometry(QtCore.QRect(228, 149, 541, 441))
        self.chartsView.setObjectName("chartsView")
        self.updateChart = QtWidgets.QPushButton(self.centralwidget)
        self.updateChart.setGeometry(QtCore.QRect(550, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateChart.setFont(font)
        self.updateChart.setObjectName("updateChart")
        self.updateChart.setText("Update")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 100, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevDate = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.prevDate.setObjectName("prevDate")
        self.horizontalLayout.addWidget(self.prevDate)
        self.currentDate = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.currentDate.setObjectName("currentDate")
        self.horizontalLayout.addWidget(self.currentDate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.updateChart.raise_()
        self.horizontalLayoutWidget.raise_()
        self.prevDate.raise_()
        self.currentDate.raise_()
        self.chartsView.raise_()
        
        layout = QtWidgets.QVBoxLayout(self.chartsView)
        static_canvas = FigureCanvasQTAgg(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)

        cursor = data.cursor()
        cursor.execute("SELECT date_rep_conf,COUNT(date_rep_conf) FROM casesByNCR GROUP BY date_rep_conf HAVING COUNT(date_rep_conf) > 1;")
        result = cursor.fetchall()
        
        df = pd.DataFrame(result, columns=['date','cases'])
        data_cases = df[['date','cases']]
        dates_x = data_cases['date'].tolist()
        cases_y= data_cases['cases'].tolist()
        
        plt.style.use('ggplot')
        
        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.plot(dates_x,cases_y,label='Cases',color='r')
        
        plt.xlabel('Dates')
        plt.ylabel('Total Cases')
        plt.title('COVID Cases by Dates (NCR)')
        
        plt.legend()
        plt.tight_layout()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVIDRecon"))
        self.updateChart.setText(_translate("MainWindow", "Update"))
        

import main_img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
