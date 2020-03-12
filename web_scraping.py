import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#help from
#https://www.youtube.com/watch?v=XQgXKtPSzUI

my_url = 'https://www.golfdigest.com/story/heres-the-prize-money-payout-for-each-golfer-at-the-2020-atandt-pebble-beach-pro-am'

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
containers = page_soup.findAll("div", {"class":"body-text"})

#prints how many containers we have
print(len(containers))

#prints html of containers section
#print(containers)
