import requests
from bs4 import BeautifulSoup as bf
# Making a GET request 1001,8001,50
res=0
movie=""
for i in range(1001,8000,50):
    r = requests.get(f'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start={i}&ref_=adv_nxt')
    # check status code for response received

    soup = bf(r.content, 'html.parser')
    # print(soup.prettify())

    s = soup.find('div', class_='lister-list')

    m=s.find_all('h3',)
    for x in s.find_all('span',class_='runtime'):
        x_=x.text.strip().split(" ")
        acc=int(x_[0])
        if acc>res:
            y=x.parent.parent.find('h3')
            z=y.find('a')
            movie=z.text
            res=acc

print(movie,res)
