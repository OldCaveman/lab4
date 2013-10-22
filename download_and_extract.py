import urllib2
import csv


def download(datetime):
    # parse out the date into the url string
    url = "http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNYTULLY1&month=10&day=32&year=2008&format=1"
    response = urllib2.urlopen(url).read()
    return response

def extract_date_time_and_temp(downloaded):
    results = []
    # use csvreader
    return results
