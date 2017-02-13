import sys
import urllib2
import re
import FB
from check import checkNOTAM, checkFirstPost
from chart import rwyCLSD, twyCLSD, portionCLSD, intersectionCLSD, savePNG
from util import getday

ADDR = "https://pilotweb.nas.faa.gov/PilotWeb/notamRetrievalByICAOAction.do?" + \
        "method=displayByICAOs&reportType=RAW&formatType=DOMESTIC&retrieveLocId=" + \
        "RCTP" + \
        "&actionType=notamRetrievalByICAOs"

linestyle = "solid"
partialnote = ""

def traverseNOTAM():
    rawNotam = urllib2.urlopen(ADDR).read()
    pat = "notamRight.*?<PRE>(.*?)</PRE>"
    allNotam = re.findall(pat, rawNotam, re.DOTALL)

    for oneNotam in allNotam:
        parseNOTAM(oneNotam)
        print "========"

def parseNOTAM(notam):
    global linestyle, partialnote

    Bpat = "B\) (.*) C"
    Cpat = "C\) (.*)"
    Bstr = re.search(Bpat, notam)
    Cstr = re.search(Cpat, notam)
    (dayin, start, end) = checkday(Bstr.group(1), Cstr.group(1))

    Dpat = "D\) (\d*)-(\d*)"
    Dstr = re.search(Dpat, notam)
    if Dstr != None:
        linestyle = "dash"
        partialnote = Dstr.group(1) + "Z - " + Dstr.group(2) + "Z"
        print partialnote
    elif dayin == "partial":
        linestyle = "dash"
        partialnote = start + "Z - " + end + "Z"
    else:
        linestyle = "solid"
        partialnote = ""

    print "dayin, " + str(dayin) + " " + start + " " + end
    if dayin:
        Epat = "E\) (.*)"
        Estr = re.search(Epat, notam, re.DOTALL)
        parseCLSD(Estr.group(1))

def checkday(starttime , endtime):
    #DEBUG
    # return (True, "", "")

    if endtime == "PERM":
        return (True, "", "")

    pat = "(\d{6})(\d{4})"
    startgroup = re.search(pat, starttime)
    start = startgroup.group(1)
    endgroup = re.search(pat, endtime)
    end = endgroup.group(1)

    today = getday()

    if start == end and start == today:
        return ("partial", startgroup.group(2), endgroup.group(2))

    res = (today >= start) and (today <= end)
    return (res, "", "")

def parseCLSD(context):
    if "CLSD" not in context:
        return False

    if "TWY" not in context:
        return False

    if "PORTION OF" in context:
        rulePortionOf(context)
        return True

    if "INT OF" in context:
        ruleIntOf(context)
        return True

    if "RWY" in context:
        ruleRWY(context)
        return True

    return ruleTWY(context)

def ruleTWY(context):
    pat = "TWY (.*) AND TWY (.*) CLSD"
    all = re.search(pat, context, re.DOTALL)

    if all != None:
        twyCLSD(all.group(1), linestyle, note=partialnote)
        twyCLSD(all.group(2), linestyle, note=partialnote)

        print "T, " + context
        return True

    pat = "TWY (.*) CLSD"
    all = re.search(pat, context, re.DOTALL)
    if all != None:
        twyCLSD(all.group(1), linestyle, note=partialnote)

        print "T, " + context
        return True

    return False

def ruleRWY(context):
    pat = "RWY (.*)/(.*) CLSD"
    all = re.search(pat, context, re.DOTALL)

    if all != None:
        rwyCLSD(all.group(1), linestyle, note=partialnote)

        print "R, " + context
        return True
    else:
        return False

def rulePortionOf(context):
    print "P, " + context

    if "BEHIND" in context:
        pat = "TWY (.*) BEHIND PRKG BAY (.*) CLSD"
        all = re.search(pat, context, re.DOTALL)
        part1 = all.group(1)
        part2 = [all.group(2)]

        pat = "(.*) AND (.*)"
        section = re.search(pat, all.group(2), re.DOTALL)
        if section != None:
            part2 = [section.group(1), section.group(2)]
            bayend = part2[1].replace('PRKG BAY ', '')
            portionCLSD(baystart=part2[0], bayend=bayend, linestyle=linestyle, note=partialnote)
        else:
            portionCLSD(baystart=part2[0], linestyle=linestyle, note=partialnote)
    elif "RWY" in context:
        pat = "TWY (.*) BTN TWY (.*)\(.*\) AND RWY (.*)\/.*\(.*\).*CLSD"
        all = re.search(pat, context, re.DOTALL)
        part1 = all.group(1)
        part2 = [all.group(2), "R"+all.group(3)]

        if all != None:
            points = []
            for item in part2:
                points.append(part1 + "_" + item)

            portionCLSD(points[0], points[1], linestyle=linestyle, note=partialnote)


    else:
        pat = "TWY (.*) BTN TWY (.*)\(.*\) AND TWY (.*)\(.*\) CLSD"
        all = re.search(pat, context, re.DOTALL)
        part1 = all.group(1)
        part2 = [all.group(2), all.group(3)]

        points = []
        for item in part2:
            points.append(part1 + "_" + item)

        portionCLSD(points[0], points[1], linestyle=linestyle, note=partialnote)

    # print points
    return

def ruleIntOf(context):
    print "I, " + context

    pat = "INT OF TWY (.*) AND TWY (.*) CLSD"
    all = re.search(pat, context, re.DOTALL)
    part1 = all.group(1)
    part2 = all.group(2)

    pat = "(.*), TWY (.*)"
    section = re.search(pat, all.group(1), re.DOTALL)
    if section != None:
        # print section.group(1)
        # print section.group(2)
        part1 = section.group(1)

    cross = part1 + "_" + part2
    print "^ " + cross

    intersectionCLSD(cross, linestyle=linestyle)

if __name__ == '__main__':
    if checkNOTAM() or checkFirstPost():
        print checkNOTAM()
        print checkFirstPost()
        today = getday()
        traverseNOTAM()
        savePNG(today)

        if len(sys.argv) == 1:
            FB.post_graph(today, "")
    else:
        print "No NOTAM"
