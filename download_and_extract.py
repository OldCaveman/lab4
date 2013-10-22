import urllib2
import csv

def download(datetime):
	# parse out the date into the url string
	url = "http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNYTULLY1&month=10&day=32&year=2008&format=1"
	response = urllib2.urlopen(url).read()
	accurate = response.replace('\n<br>', "")
	return accurate

def extract_date_time_and_temp(downloaded):
	results = []
	for measurement in downloaded.split("\n"):
		interim = measurement.split(',')
		results.append(interim[0:1])
	# use csvreader
	return results

for measurement in downloaded.split("\n"):
	result = measurement.split(',')
