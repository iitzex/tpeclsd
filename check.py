import urllib2
import re
from util import getnextday, getday
from datetime import date, datetime, timedelta

ADDR = "https://pilotweb.nas.faa.gov/PilotWeb/notamRetrievalByICAOAction.do?" + \
       "method=displayByICAOs&reportType=RAW&formatType=DOMESTIC&retrieveLocId=" + \
       "RCTP" + \
       "&actionType=notamRetrievalByICAOs"

def checkNOTAM():
    rawNotam = urllib2.urlopen(ADDR).read()
    pat = "notamRight.*?<PRE>(.*?)</PRE>"
    allNotam = re.findall(pat, rawNotam, re.DOTALL)

    oldList = readList()
    # print oldList

    newList = []
    result = False
    for oneNotam in allNotam:
        head = getHead(oneNotam)
        if head != None:
            newList.append(head)

    # print newList

    if oldList != newList:
        print oldList
        print newList
        print "not match"
        f = open('list.txt', 'w')
        for item in newList:
            f.write(item+"\n")
        return True
    else:
        return result

def getHead(context):
    Lpat = "(A.*/.*) NOTAM.*"
    Lstr = re.search(Lpat, context)

    Epat = "E\) (.*) CLSD"
    Estr = re.search(Epat, context, re.DOTALL)

    if Lstr != None and Estr != None:
        return Lstr.group(1)

    return None

def readList():
    f = open('list.txt', 'r')
    notamList = [line.rstrip('\n') for line in f]

    return notamList

def checkFirstPost():

    day = getday()

    daylist = readDay()
    if day not in daylist:
        f = open('day.txt', 'w')
        f.write(day)
        return True
    else:
        return False

def readDay():
    f = open('day.txt', 'r')
    day = [line.rstrip('\n') for line in f]

    return day

if __name__ == "__main__":
    print checkFirstPost()
    fmt = "%y%m%d,%H:%M:%S"
    print datetime.utcnow().strftime(fmt)
