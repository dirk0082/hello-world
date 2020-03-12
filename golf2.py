#different approach to find the table(s) from a golf website

import BeautifulSoup

def get_tables(htmldoc):
    soup = BeautifulSoup.BeautifulSoup(htmldoc)
    return soup.findAll('table')
