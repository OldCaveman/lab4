
import datetime
import urllib
import csv
from download_and_extract import*

url = 'http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNYTULLY1&month=%i&day=%i&year=%i&format=1'

day1 = datetime.date(2006, 1,1)

for i in range(1096):
    thisTime = day1 + datetime.timedelta(i)
    downloaded = download(thisTime)
    extracted = extract(downloaded)
    with open(Caven_Tullydata.csv, 'wa') as csvfile:
        mywriter = csv.writer(csvfile)
        mywriter.writerows(extracted)
        print extracted

#Split temp and datetime strings
##        else:
##            m = j.split(',')
##            n = m[0]
#Handle exceptions (not sure why these are occuring really. url contains bad or non-existent data?)
##            try:
##                o = m[1]
##            except:
##                IndexError
#write temp and datetime to output file
##            outp.write(n + ',' + o + '\n')
##            print n
##            print o
##        a = a + 1
##outp.close()

