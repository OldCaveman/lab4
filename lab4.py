
import time
import datetime
import urllib
import webbrowser
import os
import csv

# data source
url = 'http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNYTULLY1&month=%i&day=%i&year=%i&format=1'
#define dates and times of data extracted
##s = '2006-1-1 00:00:00'
##t = time.strptime(s, '%Y-%m-%d %H:%M:%S')
#create a file for the data to be saved
##os.chdir(r'H:\Desktop')
##inp = file('Tullydata.csv', 'r')
outp = file('Caven_Tullydata.csv', 'w')
#begin saved data file with header of dates
##header = outp.readline().strip().split(',')

#FAILED ATTEMPT
##with open('TullyData.csv', 'r') as csvfile:
##    x = csv.reader(csvfile, delimiter=' ', quotechar='|')
##    for row in x:
##        print ', '.join(x)

#FAILED ATTEMPT
##for i in range(1,1096):
##    thisTime = "2006 %i" % (i)
##    structTime = time.strptime(thisTime, '%Y %j')
##    print url % (structTime[0], structTime[1], structTime[2])

day1 = datetime.date(2006, 1,1)
##day1 + datetime.timedelta(1)
##day1 + datetime.timedelta(1096)
##day1.month
##day1.year
##day1.day
##for i in range(1096):
##    thisDate = day1 + datetime.timedelta(i)
##    print url % (thisDate.year, thisDate.day, thisDate.month)

#FAILED ATTEMPT??
##for i in range(1,1096):
##    for j in (1,13):
##        for day in range(1,32):
##            url%(i, day, j)
##            m = urllib.urlopen(url)
##            html = m.read()
##            data = inp.readline().strip().split(',')
##            print html
##      for h in range(1, 1096):

#FAILED ATTEMPT        
##for j in range(1, 1096):
##    thisTime = "2007 %i" % (j)
##    print time.strptime(thisTime, "%Y %j")
##
##for k in range(1, 1096):
##    thisTime = "2008 %i" % (k)
##    print time.strptime(thisTime, "%Y %j")

#Provide true statements for reference
a = 0
b = 1
#Loop through three years of days (+1 for leap year 2008)
for i in range(1096):
    thisTime = day1 + datetime.timedelta(i)
    data = url % (thisTime.month, thisTime.day, thisTime.year)
    time = urllib.urlopen(data)
#loop through times
    for j in time:
        if a == 0:
            print ''
        elif a == 2:
            if b == 1:
#write header "datetime and temp"
                header = j.split(',')
                outp.write(header[0] + "," + header[1] + "\n")
                b = 2
        elif j == '<br>\n':
            print ''
#Split temp and datetime strings
        else:
            m = j.split(',')
            n = m[0]
#Handle exceptions (not sure why these are occuring really. url contains bad or non-existent data?)
            try:
                o = m[1]
            except:
                IndexError
#write temp and datetime to output file
            outp.write(n + ',' + o + '\n')
##            print n
##            print o
        a = a + 1
outp.close()

    







