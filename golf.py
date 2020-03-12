#program that scrapes a table from golf news net and prints
#the html of the table in the terminal

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = 'https://thegolfnewsnet.com/golfnewsnetteam/2020/02/09/2020-att-pebble-beach-pro-am-money-purse-winners-share-prize-money-payout-118206/'

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

title = page_soup.find("title")
print(title)

containers = page_soup.findAll("table", {"class":"tablesorter"} )

print(len(containers))

print(containers)
