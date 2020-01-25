#https://www.wildberries.ru/brands/bayramali?pagesize=200
import random
import time

import requests
from lxml import html
import re


# with open('/home/stani/1list.html', 'r') as myfile:
#   html_file = myfile.read()
from textilstock.cart.wlb import getNomenclature, wirteResToCsv

r = requests.get("https://www.wildberries.ru/brands/bayramali?pagesize=200")
html_file = r.text



urls = re.findall("https[^\"]*detail.aspx[^\"]*", html_file)

res = dict()
for u in urls:
  print(u)
  r = requests.get(u)
  nomen = getNomenclature(r.text)
  res.update(nomen)
  time.sleep(1+ random.randint(1, 7000)/1000)
  wirteResToCsv(res)

