# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import news_ui
from WebScraping import DOH_Scrapper
from WebScraping import COVID19_Scrapper
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from pandas.plotting import register_matplotlib_converters
import webbrowser
import numpy as np
import pandas as pd
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
             
    def openOverview(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 616)
        MainWindow.setToolTipDuration(0)
        MainWindow.setFixedSize(781, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 891, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 0, 20, 641))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.total_cases = QtWidgets.QLabel(self.centralwidget)
        self.total_cases.setEnabled(True)
        self.total_cases.setGeometry(QtCore.QRect(240, 130, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.total_cases.setFont(font)
        self.total_cases.setAutoFillBackground(False)
        self.total_cases.setAlignment(QtCore.Qt.AlignCenter)
        self.total_cases.setObjectName("total_cases")
        self.total_death = QtWidgets.QLabel(self.centralwidget)
        self.total_death.setGeometry(QtCore.QRect(390, 260, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.total_death.setFont(font)
        self.total_death.setAlignment(QtCore.Qt.AlignCenter)
        self.total_death.setObjectName("total_death")
        self.total_recovered = QtWidgets.QLabel(self.centralwidget)
        self.total_recovered.setGeometry(QtCore.QRect(360, 390, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.total_recovered.setFont(font)
        self.total_recovered.setAlignment(QtCore.Qt.AlignCenter)
        self.total_recovered.setObjectName("total_recovered")
        self.title_status = QtWidgets.QLabel(self.centralwidget)
        self.title_status.setGeometry(QtCore.QRect(230, 10, 571, 81))
        font = QtGui.QFont()
        font.setFamily("PT Sans Caption")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.title_status.setFont(font)
        self.title_status.setObjectName("title_status")
      
        self.cases_textBrowser = QtWidgets.QLabel(self.centralwidget)
        self.cases_textBrowser.setGeometry(QtCore.QRect(370, 180, 261, 61))
        self.cases_textBrowser.setObjectName("cases_textBrowser")
        self.cases_textBrowser.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.cases_textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.death_textBrowser = QtWidgets.QLabel(self.centralwidget)
        self.death_textBrowser.setGeometry(QtCore.QRect(370, 310, 261, 61))
        self.death_textBrowser.setObjectName("death_textBrowser")
        self.death_textBrowser.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.death_textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.recoverd_textBrowser = QtWidgets.QLabel(self.centralwidget)
        self.recoverd_textBrowser.setGeometry(QtCore.QRect(370, 440, 261, 61))
        self.recoverd_textBrowser.setObjectName("recoverd_textBrowser")
        self.recoverd_textBrowser.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.recoverd_textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        fontfortextbrowser = QtGui.QFont()
        fontfortextbrowser.setFamily("Montserrat")
        fontfortextbrowser.setPointSize(25)
        fontfortextbrowser.setBold(False)
        fontfortextbrowser.setWeight(100)
        self.cases_textBrowser.setFont(fontfortextbrowser)
        self.death_textBrowser.setFont(fontfortextbrowser)
        self.recoverd_textBrowser.setFont(fontfortextbrowser)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 160, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.overview_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overview_button.setFont(font)
        self.overview_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.overview_button.setToolTipDuration(0)
        self.overview_button.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/flat-icon-png-40260.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.overview_button.setIcon(icon)
        self.overview_button.setIconSize(QtCore.QSize(40, 40))
        self.overview_button.setObjectName("overview_button")
        self.verticalLayout.addWidget(self.overview_button)


        #News_UI
        self.doh_list = news_ui.news_ui(self.centralwidget)
        self.doh_list.setObjectName('doh_list')
        ws = DOH_Scrapper.DOH_Scrapper()
        ws.run()
        rawData = ws.getData()
        array_data = []
        for x in rawData:
            data = news_ui.News()
            data.ArticleName = x[0]
            data.ArticleLink = x[1]
            array_data.append(data)
        self.doh_list.add_News(array_data)
        #/News UI

        


        self.charts_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.charts_button.setFont(font)
        self.charts_button.setToolTipDuration(1)
        self.charts_button.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/kisspng-computer-icons-bar-chart-charts-5abed4a903cbf3.1869123215224557210156.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.charts_button.setIcon(icon1)
        self.charts_button.setIconSize(QtCore.QSize(40, 40))
        self.charts_button.setObjectName("charts_button")
        self.verticalLayout.addWidget(self.charts_button)
        self.location_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.location_button.setFont(font)
        self.location_button.setAutoFillBackground(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/icons8-location-64.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.location_button.setIcon(icon2)
        self.location_button.setIconSize(QtCore.QSize(40, 40))
        self.location_button.setObjectName("location_button")
        self.verticalLayout.addWidget(self.location_button)
        self.patterns_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.patterns_button.setFont(font)
        self.patterns_button.setAutoFillBackground(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/iconfinder_10_1516234.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.patterns_button.setIcon(icon3)
        self.patterns_button.setIconSize(QtCore.QSize(40, 40))
        self.patterns_button.setObjectName("patterns_button")
        self.verticalLayout.addWidget(self.patterns_button)

        self.news_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.news_button.setFont(font)
        self.news_button.setAutoFillBackground(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/news.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.news_button.setIcon(icon4)
        self.news_button.setIconSize(QtCore.QSize(40,40))
        self.verticalLayout.addWidget(self.news_button)


        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(200, 0, 16, 711))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(20, 490, 158, 39))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_button.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/25f03a917cfb2c9beb28d0ffcd236ffa.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.about_button.setIcon(icon4)
        self.about_button.setIconSize(QtCore.QSize(30, 30))
        self.about_button.setObjectName("about_button")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 71, 81))
        self.label.setStyleSheet("image: url(:/header/Images/philippines.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 161, 61))
        self.label_3.setStyleSheet("image: url(:/header/Images/mapua-logo2.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 791, 721))
        self.label_2.setStyleSheet("background-image: url(:/bg/Images/bg-main4.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.total_cases.raise_()
        self.total_death.raise_()
        self.total_recovered.raise_()
        self.title_status.raise_()

        self.cases_textBrowser.raise_()
        self.death_textBrowser.raise_()
        self.recoverd_textBrowser.raise_()
        self.verticalLayoutWidget.raise_()
        self.line_3.raise_()
        self.about_button.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.doh_list.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")


        #Charts UI
        self.chartsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.chartsView.setGeometry(QtCore.QRect(228, 159, 541, 421))
        self.chartsView.setObjectName("chartsView")
        self.updateChart_button = QtWidgets.QPushButton(self.centralwidget)
        self.updateChart_button.setGeometry(QtCore.QRect(610, 110, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateChart_button.setFont(font)
        self.updateChart_button.setObjectName("updateChart_button")
        self.updateChart_button.setText("Update")
        self.guide1 = QtWidgets.QLabel(self.centralwidget)
        self.guide1.setGeometry(QtCore.QRect(230, 100, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guide1.setFont(font)
        self.guide1.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.guide1.setObjectName("guide1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 120, 371, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevDate = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.prevDate.setMinimumDate(QtCore.QDate(2020, 3, 8))
        self.prevDate.setDate(QtCore.QDate(2020, 3, 8))
        self.prevDate.setObjectName("prevDate")
        self.horizontalLayout.addWidget(self.prevDate)
        self.currentDate = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.currentDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 3, 9), QtCore.QTime(0, 0, 0)))
        self.currentDate.setMinimumDate(QtCore.QDate(2020, 3, 9))
        self.currentDate.setDate(QtCore.QDate(2020, 3, 9))
        self.currentDate.setObjectName("currentDate")
        self.horizontalLayout.addWidget(self.currentDate)
        self.updateChart_button.raise_()
        self.horizontalLayoutWidget.raise_()
        self.prevDate.raise_()
        self.currentDate.raise_()
        self.chartsView.raise_()
        self.guide1.raise_()
        self.chartsView.hide()
        self.updateChart_button.hide()
        self.horizontalLayoutWidget.hide()
        self.prevDate.hide()
        self.currentDate.hide()
        self.guide1.hide()
        self.layoutlim = 0
        #/ChartUI 
        
        #Location UI
        self.locationView = QtWidgets.QGraphicsView(self.centralwidget)
        self.locationView.setGeometry(QtCore.QRect(230, 110, 541, 471))
        self.locationView.setObjectName("locationView")
        self.locationView.raise_()
        self.locationView.hide()
        
        #Patterns UI
        fontforLabel = QtGui.QFont()
        fontforLabel.setFamily("Montserrat")
        fontforLabel.setPointSize(17)
        fontforLabel.setBold(False)
        fontforLabel.setWeight(50)
        self.textBrowser_Current = QtWidgets.QLabel(self.centralwidget)
        self.textBrowser_Current.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.textBrowser_Current.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_Current.setGeometry(QtCore.QRect(270, 310, 201, 61))
        self.textBrowser_Current.setObjectName("textBrowser_Current")
        self.textBrowser_Tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.textBrowser_Tomorrow.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.textBrowser_Tomorrow.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_Tomorrow.setGeometry(QtCore.QRect(540, 310, 201, 61))
        self.textBrowser_Tomorrow.setObjectName("textBrowser_Tomorrow")
        fontfortextbrowser1 = QtGui.QFont()
        fontfortextbrowser1.setFamily("Montserrat")
        fontfortextbrowser1.setPointSize(25)
        fontfortextbrowser1.setBold(False)
        fontfortextbrowser1.setWeight(100)
        self.textBrowser_Current.setFont(fontfortextbrowser1)
        self.textBrowser_Tomorrow.setFont(fontfortextbrowser1)
        self.label_Current = QtWidgets.QLabel(self.centralwidget)
        self.label_Current.setGeometry(QtCore.QRect(320, 260, 231, 61))
        self.label_Current.setObjectName("label_Current")
        self.label_Current.setFont(fontforLabel)
        self.label_Tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.label_Tomorrow.setGeometry(QtCore.QRect(525, 260, 231, 61))
        self.label_Tomorrow.setObjectName("label_Tomorrow")
        self.label_Tomorrow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tomorrow.setFont(fontforLabel)
        self.label_Current.raise_()
        self.label_Tomorrow.raise_()
        #/Patterns UI

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Data for Overview
        self.overview_data = COVID19_Scrapper.COVID19_Scrapper()
        data = []
        data = self.overview_data.x
        self.cases_textBrowser.setText(data[0])
        self.death_textBrowser.setText(data[1])
        self.recoverd_textBrowser.setText(data[2])
        #/Data for Overview

        self.updateChart_button.clicked.connect(self.on_update_chart_clicked)
        self.charts_button.clicked.connect(self.on_charts_clicked)
        self.patterns_button.clicked.connect(self.on_patterns_clicked)
        self.location_button.clicked.connect(self.on_location_clicked)
        self.overview_button.clicked.connect(self.on_overview_clicked)
        self.news_button.clicked.connect(self.on_news_clicked)
        self.on_overview_clicked()

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVIDRecon"))
        self.total_cases.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">TOTAL CASES</span></p></body></html>"))
        self.total_death.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">TOTAL DEATHS</span></p></body></html>"))
        self.total_recovered.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">TOTAL RECOVERED</span></p></body></html>"))
        self.title_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">COVID-19 Philippines</span></p></body></html>"))
        self.overview_button.setToolTip(_translate("MainWindow", "Show Summary"))
        self.overview_button.setText(_translate("MainWindow", " OVERVIEW"))
        self.charts_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Show latest cases of COVID-19.</p></body></html>"))
        self.charts_button.setText(_translate("MainWindow", " CHARTS"))
        self.location_button.setText(_translate("MainWindow", " LOCATION"))
        self.patterns_button.setText(_translate("MainWindow", " PATTERNS"))
        self.about_button.setText(_translate("MainWindow", "  ABOUT US"))
        
        self.label_Current.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">Current</span></p></body></html>"))
        self.label_Tomorrow.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;text-align:center;\">Next 24 Hours</span></p></body></html>"))
        self.about_button.clicked.connect(lambda: webbrowser.open('https://vppexis.github.io/CPE106L-ProjectCovidRecon/'))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
   
        self.news_button.setText(_translate("MainWindow", "DOH NEWS"))
        self.about_button.clicked.connect(lambda: webbrowser.open('https://vppexis.github.io/CPE106L-ProjectCovidRecon/'))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.guide1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Date/Month/Year</span></p></body></html>"))

    def data_gather(self):
        cursor = data.cursor()
        cursor.execute("SELECT date_rep_conf,COUNT(date_rep_conf) FROM casesByNCR GROUP BY date_rep_conf HAVING COUNT(date_rep_conf) > 1;")
        result = cursor.fetchall()  
        self.df = pd.DataFrame(result, columns=['date','cases'])
        self.data_cases = self.df[['date','cases']]
        self.date_x = self.data_cases['date']
        self.cases_y = self.data_cases['cases']
        
    def setup_chart(self):
        
        if self.layoutlim == 0:
            # Date gather
            cursor = data.cursor()
            cursor.execute("SELECT date_rep_conf,COUNT(date_rep_conf) FROM casesByNCR GROUP BY date_rep_conf HAVING COUNT(date_rep_conf) > 1;")
            result = cursor.fetchall()  
            self.df = pd.DataFrame(result, columns=['date','cases'])
            self.data_cases = self.df[['date','cases']]
            date_x = self.data_cases['date']
            cases_y = self.data_cases['cases']
            
            # Making the layout for the graph
            self.layout = QtWidgets.QVBoxLayout(self.chartsView)
            self.dynamic_canvas = FigureCanvasQTAgg(Figure(figsize=(5, 3)))
            self.layout.addWidget(self.dynamic_canvas)
                
            x = date_x
            y = np.cumsum(cases_y)
            
            dynamic_ax = self.dynamic_canvas.figure.subplots()
            self.dynamic_canvas.figure.autofmt_xdate() 
            self.dynamic_canvas.figure.fmt_xdata = mdates.DateFormatter('%y-%m-%d')
            self.recovered_chart()
            self.died_chart()
            dynamic_ax.plot(x,y,label='Cases',color='r')
            dynamic_ax.plot(self.R_x,self.R_y,label='Recovered',color='g')  
            dynamic_ax.plot(self.D_x,self.D_y,label='Died',color='b') 
            dynamic_ax.legend()
            dynamic_ax.set_xlabel('Dates of Report')
            dynamic_ax.set_ylabel('Population Affected')
            dynamic_ax.set_title('COVID-19 Cases')
            self.layoutlim = 1
            
    def recovered_chart(self):
        
        cursor = data.cursor()
        if self.layoutlim == 0:
            cursor.execute("SELECT date_rep_conf, Count(health_status) from casesByNCR where health_status = 'Recovered'GROUP BY date_rep_conf;")
            result = cursor.fetchall()  
        else:
            cursor.execute("SELECT date_rep_conf,Count(health_status)from casesByNCR where (health_status = 'Recovered') And date_rep_conf between %s AND %s group by date_rep_conf" , (self.minDate,self.maxDate))
            result = cursor.fetchall()
            
        df = pd.DataFrame(result, columns=['date','recovered'])
        data_cases = df[['date','recovered']]
        self.R_x = data_cases['date']
        self.R_y = np.cumsum(data_cases['recovered'])
       
        
    def died_chart(self):
        
        cursor = data.cursor()
        if self.layoutlim == 0:
            cursor.execute("SELECT date_rep_conf, Count(health_status) from casesByNCR where health_status = 'Died'GROUP BY date_rep_conf;")
            result = cursor.fetchall()
        else:
            cursor.execute("SELECT date_rep_conf,Count(health_status)from casesByNCR where (health_status = 'Died') And date_rep_conf between %s AND %s group by date_rep_conf", (self.minDate,self.maxDate))
            result = cursor.fetchall()
        df = pd.DataFrame(result, columns=['date','Died'])
        data_cases = df[['date','Died']]
        self.D_x = data_cases['date']
        self.D_y = np.cumsum(data_cases['Died'])
            
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
        self.recovered_chart()
        self.died_chart()
        dynamic_ax.plot(x,y,label='Cases',color='r')
        dynamic_ax.plot(self.R_x,self.R_y,label='Recovered',color='g')  
        dynamic_ax.plot(self.D_x,self.D_y,label='Died',color='b') 
        dynamic_ax.legend()
        dynamic_ax.set_xlabel('Dates of Report')
        dynamic_ax.set_ylabel('Population Affected')
        dynamic_ax.set_title('COVID-19 Cases')
        
    def delete_canvas(self):
        self.dynamic_canvas.deleteLater()
          
    def hide_overview_ui(self):
        self.total_cases.hide()
        self.total_death.hide()
        self.total_recovered.hide()
        self.cases_textBrowser.hide()
        self.death_textBrowser.hide()
        self.recoverd_textBrowser.hide()
    
    def hide_charts_ui(self):
        self.chartsView.hide()
        self.updateChart_button.hide()
        self.horizontalLayoutWidget.hide()
        self.prevDate.hide()
        self.currentDate.hide()
        self.guide1.hide()

        
    def hide_location_ui(self):
        self.locationView.hide()

    def hide_patterns_ui(self):
        self.textBrowser_Current.hide()
        self.textBrowser_Tomorrow.hide()
        self.label_Current.hide()
        self.label_Tomorrow.hide()

    def hide_news_ui(self):
        self.doh_list.hide()

    

    #show methods
    def on_overview_ui(self):
        self.total_cases.show()
        self.total_death.show()
        self.total_recovered.show()
        self.cases_textBrowser.show()
        self.death_textBrowser.show()
        self.recoverd_textBrowser.show()

    def on_charts_ui(self):
        self.chartsView.show()
        self.updateChart_button.show()
        self.horizontalLayoutWidget.show()
        self.prevDate.show()
        self.currentDate.show()
        self.guide1.show()
        self.setup_chart()
        

    def on_location_ui(self):
        self.locationView.show()

    def on_patterns_ui(self):
        self.textBrowser_Current.show()
        self.textBrowser_Tomorrow.show()
        self.label_Current.show()
        self.label_Tomorrow.show()
        
    
    def on_news_ui(self):
        self.doh_list.show()


    #button clicked methods
    def on_overview_clicked(self):
        self.on_overview_ui()
        self.hide_charts_ui()
        self.hide_location_ui()
        self.hide_patterns_ui()
        self.hide_news_ui()
   
    def on_charts_clicked(self):
        self.hide_overview_ui()
        self.on_charts_ui()
        self.hide_location_ui()
        self.hide_patterns_ui()
        self.hide_news_ui()
        
    def on_update_chart_clicked(self):
        
        if self.layoutlim == 0:
            self.setup_chart()    
        else:
            self.delete_canvas()
            self.update_chart()
        
    def on_location_clicked(self):
        self.hide_overview_ui()
        self.hide_charts_ui()
        self.on_location_ui()
        self.hide_patterns_ui()
        self.hide_news_ui()
        

    def on_patterns_clicked(self):
        self.hide_overview_ui()
        self.hide_charts_ui()
        self.hide_location_ui()
        self.on_patterns_ui()
        self.hide_news_ui()

    def on_news_clicked(self):
        self.hide_overview_ui()
        self.hide_charts_ui()
        self.hide_location_ui()
        self.hide_patterns_ui()
        self.on_news_ui()

import main_img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)


    #Sets window icon
    app.setWindowIcon(QtGui.QIcon('Images/logo.png'))

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #Sets to Frameless Window
    #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    MainWindow.show()
    sys.exit(app.exec_())
