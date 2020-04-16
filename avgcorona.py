from urllib.request import Request, urlopen
import csv
import requests
from collections import Counter
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime


CSV_URL = 'http://covidtracking.com/api/states/daily.csv'

#Empty dictionaries to fill with new positive cases for today, yesterday, and two days prior respectively
case_increases_1 = {}
case_increases_2 = {}
case_increases_3 = {}

#set variables for dates to generalize the program, as opposed to searching specific dates
yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.strftime('%Y%m%d')

two_days_prior_ago = date.today() - timedelta(days=2)
two_days_prior_ago = two_days_prior_ago.strftime('%Y%m%d')

three_days_prior_ago = date.today() - timedelta(days=3)
three_days_prior_ago = three_days_prior_ago.strftime('%Y%m%d')

#establish connection and download csv
with requests.Session() as s:
    download = s.get(CSV_URL)
    #print(response['headers'])
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
	#iterate throw rows to fill dictionaries and sum the positive test cases
    for row in my_list:
         date = row[0]
         state = row[1]
         pos_increase = row[23]
         if date == yesterday:
            if state in case_increases_1:
                case_increases_1[state] = pos_increase[state] + pos_increase
            else:
                case_increases_1[state] = pos_increase
         if date == two_days_prior_ago:
            if state in case_increases_2:
                case_increases_2[state] = case_increases_2[state] + pos_increase
            else:
                case_increases_2[state] = pos_increase
         if date == three_days_prior_ago:
            if state in case_increases_3:
                case_increases_3[state] = case_increases_3[state] + pos_increase
            else:
                case_increases_3[state] = pos_increase

#s.config['keep_alive'] = False

#Dictionary to fill with the average of the three dates for each state
moving_avg = {}

for location_1 in case_increases_1:
    moving_avg[location_1] = str(((int(case_increases_1[location_1])+int(case_increases_2[location_1])+int(case_increases_3[location_1]))//3))

#Dictionary to fill with the float of the values in monving_dictionary, which were stored as strings
new_moving_avgs = {}

for key, value in moving_avg.items():
     new_moving_avgs[key] = float(value)

print(new_moving_avgs)

# Finding 3 highest values
k = Counter(new_moving_avgs)

high = k.most_common(3)

print("Time To Stay Inside...")

for i in high:
    print(i[0]," :",i[1]," ")
