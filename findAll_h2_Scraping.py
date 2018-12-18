from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
    html = urlopen("https://blog.scrapinghub.com/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    contador = 0
    tags = res.findAll("div", {"class": "byline"})
    #tags = res.findAll("link")
    for tag in tags:
        #print(tag.getText())   #Solo devuelve el texto de la etiqueta.
        contador += 1
        print(tag)  #Devuelve la URL más el texto de la etiqueta.
finally:
    print(contador)