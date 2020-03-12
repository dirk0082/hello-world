import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://thegolfnewsnet.com/golfnewsnetteam/2020/02/09/2020-att-pebble-beach-pro-am-money-purse-winners-share-prize-money-payout-118206/'

#opening up connection, grabbing page
uClient = uReq(my_url)
#offloads content into usable variable
page_html = uClient.read()

#prints html page
#print(page_html)

#closes connection
uClient.close

#html parsing
page_soup = soup(page_html, 'html.parser')

#prints header 1
#print(page_soup.h1)

#prints p tag
#print(page_soup.p)

#grabs each product
containers = page_soup.findAll("table")

#prints how many containers we have
print(len(containers))

#prints html of containers section
#print(containers)
