import requests
from bs4 import BeautifulSoup


#Allows an access to the website.
with requests.Session() as se:
    se.headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Language' : 'en'
    }

#Gets the URL of the website.
result = se.get('https://www.inquirer.net/')

#If it returns 200 then it is connected. Otherwise, it is not.
#print(result.status_code)

src = result.content
soup = BeautifulSoup(src, 'lxml')

#print(soup.find_all('a', limit=1))


urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    try:
        if 'href' in a_tag.attrs:
            urls.append(a_tag.attrs['href'])
    except:
        pass

for x in urls:
    print(x)