import certifi
certifi.where()
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/certifi/cacert.pem'
from urllib.request import urlopen
import html5lib
from bs4 import BeautifulSoup
html = urlopen("http://www.python.org/")
res = BeautifulSoup(html.read(),"html5lib");
print(res.title)