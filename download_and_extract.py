import urllib2
import csv
import datetime

def download(thisTime):
	# parse out the date into the url string
	url = "http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNYTULLY1&month=%i&day=%i&year=%i&format=1"
	data = url % (thisTime.month, thisTime.day, thisTime.year)
	response = urllib2.urlopen(data).read()
	accurate = response.replace('\n<br>', "")
	return accurate

def extract_date_time_and_temp(downloaded):
	results = []
	for measurement in downloaded.split("\n"):
		interim = measurement.split(',')
		if len(interim) > 1:
			result.append(interim[0:2])

	return results