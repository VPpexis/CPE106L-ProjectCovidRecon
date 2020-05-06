import requests
import pandas as pd
from bs4 import BeautifulSoup


class DOH_Scrapper():
    def __init__(self):
        self.articleName = []
        self.articleLink = []


    def run(self):
        #Allows an access to the website.
        with requests.Session() as se:
            se.headers = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66',
                'Accept-Encoding' : 'gzip, deflate',
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'Accept-Language' : 'en'
            }


        #Gets the URL of the website.
        result = se.get('https://www.doh.gov.ph/press-releases', verify=False)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')


        for content in soup.find_all('div', attrs = {'class':'region region-content'}):
            for tags in content.find_all('span', attrs = {'class':'field-content'}):
                for rows in tags.find_all('a'):
                    self.articleName.append(rows.getText())
                    self.articleLink.append('https://www.doh.gov.ph' + rows['href'])

        d = {'Article Name': self.articleName, 'Link': self.articleLink}
        self.df = pd.DataFrame(data=d)
    
    def getData(self):
        return self.df.values.tolist()
        

if __name__ == '__main__':
    ws = DOH_Scrapper()
    ws.run()
    dataNews = ws.getData()

    for x in dataNews:
        print(x[1])