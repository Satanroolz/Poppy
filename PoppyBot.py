

#Rusty Moose Server Pop Scraper aka Poppy

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

my_url = 'https://moose.gg/ssm'

#Opening connection, grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Grabs Moose Main info
container = page_soup.findALL("div",{"ipsColumns"})

container.div.h6