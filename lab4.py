
import datetime
import urllib
import csv
from download_and_extract import*

url = 'http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNYTULLY1&month=%i&day=%i&year=%i&format=1'

day1 = datetime.date(2006, 1,1)

with open('Caven_Tullydata.csv', 'a') as csvfile:
    mywriter = csv.writer(csvfile)
for i in range(1096):
    thisTime = day1 + datetime.timedelta(i)
    downloaded = download(thisTime)
    extracted = extract(downloaded)
    mywriter.writerows(extracted)
    print extracted

