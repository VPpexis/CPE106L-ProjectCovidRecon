import requests
import pandas as pd
from bs4 import BeautifulSoup

class COVID19_Scrapper():
    def __init__(self):
        result = requests.get('https://www.covid19.gov.ph/')
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        self.x = []


        for content in soup.find_all('span', attrs = {'class':'elementor-counter-number'}):
            self.x.append(content.get('data-to-value'))

        

if __name__ == '__main__':
    datascann = COVID19_Scrapper()

    print(datascann.x)
            
