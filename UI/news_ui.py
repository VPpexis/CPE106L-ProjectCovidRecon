from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class news_ui(QtWidgets.QListWidget):
    def __init__(self, *args, **kwargs):
        super(news_ui, self).__init__(*args, **kwargs)
        self.setGeometry(QtCore.QRect(260, 130, 520, 450))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWordWrap(True)
        self.setSpacing(5)
        self.itemClicked.connect(self.listwidgetclicked)

    def add_News(self, NewsList):
        self.NewsList = NewsList  
        for x in self.NewsList:
            self.addItem(x.ArticleName)

    def listwidgetclicked(self, item):
        for x in  self.NewsList:
            if item.text() == x.ArticleName:
                if x.ArticleLink == '':
                    criticalMessage = QtWidgets.QMessageBox()
                    criticalMessage.setIcon(QtWidgets.QMessageBox.Warning)
                    criticalMessage.setText('Warning')
                    criticalMessage.setInformativeText('No Link was provided')
                    criticalMessage.exec_()
                    return
                webbrowser.open(x.ArticleLink)
                break
    
class News():
    def __init__(self):
        self.ArticleName = ''
        self.ArticleLink = ''


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    news = news_ui()

    x = []

    news1 = News()
    news1.ArticleName = 'GOVERNMENT LAUNCHES PUBLIC-PRIVATE TASK FORCE T3 (TEST, TRACE AND TREAT) TO SIGNIFICANTLY EXPAND RT-PCR TESTING CAPACITY'
    news1.ArticleLink = 'https://www.doh.gov.ph/doh-press-release/government-launches-public-private-task-force-T3'
    news2 = News()
    print(news1.ArticleLink)
    news2.ArticleName = 'DOH, DFA RECEIVE 700 TEST KITS FOR 35,000 TESTS FROM ROK'
    news2.ArticleLink = 'https://www.doh.gov.ph/doh-press-release/doh-fda-receive-700-test-kits-for-35k-tests-from-rok'

    x.append(news1)
    x.append(news2)

    news.add_News(x)
    news.show()
    app.exec_()

