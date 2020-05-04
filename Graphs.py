from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from pandas.plotting import register_matplotlib_converters
import webbrowser
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
        self.layoutlim =0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chartsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.chartsView.setGeometry(QtCore.QRect(228, 149, 541, 441))
        self.chartsView.setObjectName("chartsView")
        self.updateChart_button = QtWidgets.QPushButton(self.centralwidget)
        self.updateChart_button.setGeometry(QtCore.QRect(550, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateChart_button.setFont(font)
        self.updateChart_button.setObjectName("updateChart_button")
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
        self.updateChart_button.raise_()
        self.horizontalLayoutWidget.raise_()
        self.prevDate.raise_()
        self.currentDate.raise_()
        self.chartsView.raise_()
        
        self.updateChart_button.clicked.connect(self._update_button)
    
    def data_gather(self):
        cursor = data.cursor()
        cursor.execute("SELECT date_rep_conf,COUNT(date_rep_conf) FROM casesByNCR GROUP BY date_rep_conf HAVING COUNT(date_rep_conf) > 1;")
        result = cursor.fetchall()  
        self.df = pd.DataFrame(result, columns=['date','cases'])
        self.data_cases = self.df[['date','cases']]
        self.date_x = self.data_cases['date']
        self.cases_y = self.data_cases['cases']
        
        
    def setup_chart(self):
        
        self.layout = QtWidgets.QVBoxLayout(self.chartsView)
        self.dynamic_canvas = FigureCanvasQTAgg(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.dynamic_canvas)
            
        x = self.date_x
        y = np.cumsum(self.cases_y)
        
        dynamic_ax = self.dynamic_canvas.figure.subplots()
        self.dynamic_canvas.figure.autofmt_xdate() 
        self.dynamic_canvas.figure.fmt_xdata = mdates.DateFormatter('%y-%m-%d')
        dynamic_ax.plot(x,y,label='Cases',color='r')
          
        dynamic_ax.legend()
        self.layoutlim = 1
    
    def update_chart(self):
        self.minDate= self.prevDate.date().toPyDate()
        self.maxDate = self.currentDate.date().toPyDate()
        cursor = data.cursor()
        cursor.execute("SELECT date_rep_conf,Count(date_rep_conf) from casesByNCR where date_rep_conf between %s AND %s group by date_rep_conf having count(date_rep_conf) > 1;", (self.minDate,self.maxDate))
        #cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
        result = cursor.fetchall()  
        df = pd.DataFrame(result, columns=['date','cases'])
        data_cases = df[['date','cases']]
        x = data_cases['date']
        y = np.cumsum(data_cases['cases'])

        self.dynamic_canvas = FigureCanvasQTAgg(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.dynamic_canvas)
        
        dynamic_ax = self.dynamic_canvas.figure.subplots()
        self.dynamic_canvas.figure.autofmt_xdate() 
        self.dynamic_canvas.figure.fmt_xdata = mdates.DateFormatter('%y-%m-%d')
        dynamic_ax.plot(x,y,label='Cases',color='r')
        dynamic_ax.legend()
        ##new_dates_x = self.data_cases['date']
        #new_df = new_dates_x.query(self.minDate <= 'date' < self.maxDate)
        #print(new_df)
        
    def delete_canvas(self):
        self.dynamic_canvas.deleteLater()
        
    def _update_button(self):
        
        self.data_gather()
        if self.layoutlim == 0:
            self.setup_chart()    
        else:
            self.delete_canvas()
            self.update_chart()
            
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVIDRecon"))
        self.updateChart_button.setText(_translate("MainWindow", "Update"))
        

import main_img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
