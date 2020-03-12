#!/usr/bin/env python3


#try and make all of this a function of the url in the clipboard
#defined as function "pay_out_finder"

import openpyxl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = 'https://thegolfnewsnet.com/golfnewsnetteam/2020/02/02/2020-waste-management-phoenix-open-money-purse-winners-share-prize-money-payout-118155/'

#establish connection
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#use BeautifulSoup to gather html
page_soup = soup(webpage, "html.parser")

#print title to verify that we have a connection
title = page_soup.find("title")
print(title)

#sift through html to find the table we want
tables = page_soup.findAll("table", {"class":"tablesorter"} )

#printed the length of tables to verify we only returned 1 table
#print(len(tables))

#massage table to return only player names and winning amounts
#cols[1] is used because 2nd column in table is player names
#cols[8] is used because 9th column in table is purse amount
#pop removes first value
players = []
for table in tables:
    rows = table.findAll("tr")
    rows.pop(0)
    for row in rows:
        cols = row.findAll("td")
        players.append({"name": cols[1].contents[0], "amount": cols[8].contents[0] })

#print table to verify we removed the two columns of the chart that we want
print(players)

#input one team from spreadsheet to work with
#work on importing excel sheet later
#first let's try and create a funciton that has the team arrays work together
#teams = [{'coworker': 'Ders', 'Dirks' 'team': ['Tiger Woods', 'Justin Thomas', 'Patrick Reed', 'Dustin Johnson']}]
#print(teams)


#results = []
#for team in teams:


#excel portion

#loads sheet names
wb = openpyxl.load_workbook('golf.xlsx')

#prints sheet names
#print(wb.sheetnames)

#set which sheet we are working with
sheet = wb['Sheet1']

#indexes data to spreadsheet

index = 2
for player in players:
        name_coordinate = "A" + str(index)
        amount_coordinate = "B" + str(index)
        print(name_coordinate)
        print(amount_coordinate)
        sheet[name_coordinate] = player["name"]
        sheet[amount_coordinate] = player["amount"]
        index = index + 1

# sheet['A1'] = containers
# tester = sheet['A1'].value
# print(tester)

wb.save('golf_post_python.xlsx')

#next idea - sift through html w/ "find name" function that
#alpha character, alpha charcter (except td)
#then uses numbers following $
#pairs those items together
#form a list/array
#set timer to run Monday Morning and send e-mail to work
