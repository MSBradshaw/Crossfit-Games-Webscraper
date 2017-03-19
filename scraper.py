import urllib2
import re
#This script needs to files to functions
#1. an input with the URLs of each chart page
#2. the output file, writes in CSV format
outfile = open("CROSSFIT.txt", 'a')
#url to the master list
#startingURL = "http://games.crossfit.com/scores/leaderboard.php?stage=0&sort=0&division=1&region=0&numberperpage=60&userid=0&competition=2&frontpage=0&expanded=1&year=14&full=1&showtoggles=0&hidedropdowns=1&showathleteac=1&athletename="
#get the name and all info
def getAthInfo(urlstring):
    page = urllib2.urlopen(urlstring).read()
    pattern = 'Athlete: .*\"'
    match = re.search(pattern, page)
    name = match.group(0)
    name = name.replace("Athlete: ","")
    name = name.replace('\"',"")
    print name
    if name is "":
        return
    outfile.write(name)
    outfile.write(",")
    #get the weight
    pattern = 'Gender:</dt><dd>(Male)|(Female)'
    match = re.search(pattern, page)
    gender = match.group(0)
    gender = gender.replace("Gender:</dt><dd>","")
    print gender
    outfile.write(gender)
    outfile.write(",")
    pattern = 'Age:</dt><dd>\d\d'
    match = re.search(pattern, page)
    age = match.group(0)
    age = age.replace("Age:</dt><dd>","")
    print age
    outfile.write(age)
    outfile.write(",")
    pattern = 'Height:</dt><dd>\d;\d{0,2}&'
    match = re.search(pattern, page)
    if not match:
        pattern = 'Height:</dt><dd>\d{1,3} cm'
        match = re.search(pattern, page)
        if not match:
            height = "--"
        else:
            height = match.group(0)
            height = height.replace('Height:</dt><dd>',"")
    else:
        h1 = re.search(">\d&", match.group(0))
        h2 = re.search(";\d{1,2}&", match.group(0))
        strh1 = h1.group(0).replace(">","")
        strh1 = strh1.replace("&","")
        strh2 = h2.group(0).replace(";","")
        strh2 = strh2.replace("&","")
        height = strh1 + "\'"
        height = height + strh2
        height = height + "\""
    print height
    outfile.write(height)
    outfile.write(",")
    pattern = 'Weight:</dt><dd>\d\d\d lb'
    match = re.search(pattern, page)
    if not match:
        pattern = "Weight:</dt><dd>\d{2,3} kg"
        match = re.search(pattern, page)
        if not match:
            weight = "--"
        else:
            weight = match.group(0)
            weight= weight.replace("Weight:</dt><dd>","")
    else:
        weight = match.group(0)
        weight= weight.replace("Weight:</dt><dd>","")
    print weight
    outfile.write(weight)
    outfile.write(",")
    pattern = 'Fran</td><td>.{2,4}'
    match = re.search(pattern, page)
    fran = match.group(0)
    fran= fran.replace("Fran</td><td>","")
    fran = fran.replace("<","")
    fran = fran.replace("/","")
    print fran
    outfile.write(fran)
    outfile.write(",")
    pattern = 'Helen</td><td>.{2,4}'
    match = re.search(pattern, page)
    helen = match.group(0)
    helen = helen.replace("Helen</td><td>","")
    helen = helen.replace("</","")
    print helen
    outfile.write(helen)
    outfile.write(",")
    pattern = 'Grace</td><td>.{2,4}'
    match = re.search(pattern, page)
    Grace = match.group(0)
    Grace = Grace.replace("Grace</td><td>","")
    Grace = Grace.replace("</","")
    print Grace
    outfile.write(Grace)
    outfile.write(",")
    pattern = 'Filthy 50</td><td>.{2,5}'
    match = re.search(pattern, page)
    Filthy = match.group(0)
    Filthy = Filthy.replace("Filthy 50</td><td>","")
    Filthy = Filthy.replace("<","")
    Filthy = Filthy.replace("/","")
    Filthy = Filthy.replace("t","")
    print Filthy
    outfile.write(Filthy)
    outfile.write(",")
    pattern = 'Fight Gone Bad</td><td>.{2,4}'
    match = re.search(pattern, page)
    Fight = match.group(0)
    Fight = Fight.replace("Fight Gone Bad</td><td>","")
    Fight = Fight.replace("<","")
    Fight = Fight.replace("/","")
    print Fight
    outfile.write(Fight)
    outfile.write(",")
    pattern = 'Sprint 400m</td><td>.{2,4}'
    match = re.search(pattern, page)
    Sprint = match.group(0)
    Sprint = Sprint.replace("Sprint 400m</td><td>","")
    Sprint = Sprint.replace("</","")
    print Sprint
    outfile.write(Sprint)
    outfile.write(",")
    pattern = 'Run 5k</td><td>.{2,5}'
    match = re.search(pattern, page)
    Run = match.group(0)
    Run = Run.replace("Run 5k</td><td>","")
    Run = Run.replace("/","")
    Run = Run.replace("/","")
    Run = Run.replace("t","")
    print Run
    outfile.write(Run)
    outfile.write(",")
    pattern = 'Clean & Jerk</td><td>\d{2,4}'
    match = re.search(pattern, page)
    if not match:
        Clean = "--"
    else:
        Clean = match.group(0)
    Clean = Clean.replace("Clean & Jerk</td><td>","")
    Clean = Clean.replace("<","")
    Clean = Clean.replace("/","")
    Clean = Clean.replace("t","")
    print Clean
    outfile.write(Clean)
    outfile.write(",")
    pattern = 'Snatch</td><td>\d{2,4}'
    match = re.search(pattern, page)
    if not match:
        Snatch = "--"
    else:
        Snatch = match.group(0)
    Snatch = Snatch.replace("Snatch</td><td>","")
    Snatch = Snatch.replace("<","")
    Snatch = Snatch.replace("/","")
    Snatch = Snatch.replace("t","")
    print Snatch
    outfile.write(Snatch)
    outfile.write(",")
    pattern = 'Deadlift</td><td>\d{2,4}'
    match = re.search(pattern, page)
    match = re.search(pattern, page)
    if not match:
        Deadlift = "--"
    else:
        Deadlift = match.group(0)
    Deadlift = Deadlift.replace("Deadlift</td><td>","")
    Deadlift = Deadlift.replace("<","")
    Deadlift = Deadlift.replace("/","")
    Deadlift = Deadlift.replace("t","")
    print Deadlift
    outfile.write(Deadlift)
    outfile.write(",")
    pattern = 'Back Squat</td><td>\d{2,4}'
    match = re.search(pattern, page)
    if not match:
        Back = "--"
    else:
        Back = match.group(0)
    Back = Back.replace("Back Squat</td><td>","")
    Back = Back.replace("<","")
    Back = Back.replace("/","")
    Back = Back.replace("t","")
    print Back
    outfile.write(Back)
    outfile.write(",")
    pattern = 'Max Pull-ups</td><td>\d{2,4}'
    match = re.search(pattern, page)
    if not match:
        Pullup = "--"
    else:
        Pullup = match.group(0)
        Pullup = Pullup.replace("Max Pull-ups</td><td>","")
        Pullup = Pullup.replace("<","")
        Pullup = Pullup.replace("/","")
        Pullup = Pullup.replace("t","")
    print Pullup
    outfile.write(Pullup)
    outfile.write("\n")
#-------------------------------
def listpagecycle(startingURL):
    masterlist = urllib2.urlopen(startingURL).read()
    urlpattern = "<td class=\"name\"><a href=\".*\""
    mylist = re.findall(urlpattern,masterlist)
    for line in mylist:
        url = line
        url = url.replace("<td class=\"name\"><a href=\"","")
        url = url.replace("\" target=\"_top\"","")
        getAthInfo(url)
#-------------------------------------
f = open('crossfitIN.txt', 'r')
for line in f:
    listpagecycle(line)
