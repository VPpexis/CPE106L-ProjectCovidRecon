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
import webbrowser
import ctypes

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


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
        self.cases_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.cases_textBrowser.setGeometry(QtCore.QRect(370, 180, 261, 61))
        self.cases_textBrowser.setObjectName("cases_textBrowser")
        self.death_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.death_textBrowser.setGeometry(QtCore.QRect(370, 310, 261, 61))
        self.death_textBrowser.setObjectName("death_textBrowser")
        self.recoverd_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.recoverd_textBrowser.setGeometry(QtCore.QRect(370, 440, 261, 61))
        self.recoverd_textBrowser.setObjectName("recoverd_textBrowser")
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


        #Data for Overview
        
        self.overview_data = COVID19_Scrapper.COVID19_Scrapper()

        data = []
        data = self.overview_data.x

        self.cases_textBrowser.setText(data[0])
        self.death_textBrowser.setText(data[1])
        self.recoverd_textBrowser.setText(data[2])
        



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

        self.hide_news_ui()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.charts_button.clicked.connect(self.on_charts_clicked)
        self.patterns_button.clicked.connect(self.on_patterns_clicked)
        self.location_button.clicked.connect(self.on_location_clicked)
        self.overview_button.clicked.connect(self.on_overview_clicked)
        self.news_button.clicked.connect(self.on_news_clicked)

    

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
        self.news_button.setText(_translate("MainWindow", "DOH NEWS"))
        self.about_button.clicked.connect(lambda: webbrowser.open('https://vppexis.github.io/CPE106L-ProjectCovidRecon/'))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))

    def on_charts_clicked(self):
        self.hide_news_ui()
        self.hide_overview_ui()

    def on_location_clicked(self):
        self.hide_news_ui()
        self.hide_overview_ui()

    def on_patterns_clicked(self):
        self.hide_news_ui()
        self.hide_overview_ui()


    def hide_overview_ui(self):
        self.total_cases.hide()
        self.total_death.hide()
        self.total_recovered.hide()
        self.cases_textBrowser.hide()
        self.death_textBrowser.hide()
        self.recoverd_textBrowser.hide()

    def hide_news_ui(self):
        self.doh_list.hide()

    def on_overview_clicked(self):
        self.hide_news_ui()
        self.total_cases.show()
        self.total_death.show()
        self.total_recovered.show()
        self.cases_textBrowser.show()
        self.death_textBrowser.show()
        self.recoverd_textBrowser.show()

    def on_news_clicked(self):
        self.hide_overview_ui()
        self.doh_list.show()

        
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
