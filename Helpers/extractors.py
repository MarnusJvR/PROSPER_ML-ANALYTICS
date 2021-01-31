# This takes input of dateTime Strings like: 2020/10/30 16:55
# Extract string values for time and date
# recieves a list of dateTimes 2020/08/03
# Returns a new list of dateTimes 2004.06.17
# Splits time from dateTime string
# returns time list in string format
from datetime import date
from datetime import datetime
import datetime

def dateStringExtractor(dateList):
    # some dates are like this: 2015/01/02
    # others are like this: 2015.01.02
    print('date extractor call recieved`')
    timeStringList = []
    dateStringList = []
    finalDateStr = ''
    # Take the first date to check what the date format is
    date= dateList[1]
    dateSt = date[:10]
    dateBool = False
    for letters in dateSt:
        if letters == '/':
            dateBool = True

    for items in dateList:
        dateString = items[:10]
        # Currently date is in this format: 2020/08/03
        # I need it in this format:2004.06.17
        if dateBool:
            for letters in dateString:
                if letters != '/':
                    finalDateStr = finalDateStr + letters
                else:
                    finalDateStr = finalDateStr + '.'
            dateStringList.append(finalDateStr)
        else:
            dateStringList.append(dateString)
        timeString = items[11:]
        timeStringList.append(timeString)
        finalDateStr = ''
    # loop through list to convert strings to date structures
    dateformated = []
    print('processing....')
    for dates in dateStringList:
        print(dates)
        new_date_object = datetime.datetime.strptime(dates, '%Y.%m.%d').date()
        dateformated.append(new_date_object)
    return timeStringList, dateformated

def weekdayExtractor(datelist):
    print('weekday extrazctor call recieved')
    weekdaylist = []
    for dates in datelist:
        weekday = dates.weekday()
        weekdaylist.append(weekday)
    return weekdaylist


# Recieves string like 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
# Converts to list containing numbers
# Remember that all positions where price breaks through levels (closing, sl, tp ect) are stored in str lists
def stringpositionextractor(valuelist):
    print('string extractor called')
    # len function starts counting from 1
    # I refer to a char in a list starting counting from 0 eg. valueList[0] is item 1 in list
    checklist = []
    if valuelist != '':
        commaposition = []
        valuelist = valuelist[:-1]
        count = 1
        for chars in valuelist:
            if chars == ',':
                commaposition.append(count)
            count = count + 1
        # first
        if len(commaposition) != 0:
            firstentry = valuelist[0:commaposition[0] - 1]
            checklist.append(int(firstentry))
        else:
            firstentry = int(valuelist)
            checklist.append(int(firstentry))
        count = 0
        # I extract the first entry before i start looping
        for positions in commaposition:
            if len(commaposition) > count + 1:
                stopnum = commaposition[count + 1] - positions
                stopnum = stopnum - 1
                stopnum = positions + stopnum
                if count < len(commaposition) - 2:
                    addnum = valuelist[positions:stopnum]
                    checklist.append(int(addnum))
            if count == len(commaposition) - 1:
                addnum = valuelist[positions:len(valuelist)]
                checklist.append(int(addnum))
            count = count + 1
    else:
        checklist.append('')
    return checklist

# Recieves string like 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
# Converts to list containing numbers
# Remember that all positions where price breaks through levels (closing, sl, tp ect) are stored in str lists
def stringdtimextractor(valuelist):
    print('String Time extractor call received')
    # len function starts counting from 1
    # I refer to a char in a list starting counting from 0 eg. valueList[0] is item 1 in list
    checklist = []
    if valuelist != '':
        commaposition = []
        valuelist = valuelist[:-1]
        count = 1
        for chars in valuelist:
            if chars == ',':
                commaposition.append(count)
            count = count + 1
        # first
        if len(commaposition) != 0:
            firstentry = valuelist[0:commaposition[0] - 1]
            checklist.append(firstentry)
        else:
            firstentry = valuelist
            checklist.append(firstentry)
        count = 0
        # I extract the first entry before i start looping
        for positions in commaposition:
            if len(commaposition) > count + 1:
                stopnum = commaposition[count + 1] - positions
                stopnum = stopnum - 1
                stopnum = positions + stopnum
                if count < len(commaposition) - 2:
                    addnum = valuelist[positions:stopnum]
                    checklist.append(addnum)
            if count == len(commaposition) - 1:
                addnum = valuelist[positions:len(valuelist)]
                checklist.append(addnum)
            count = count + 1
    else:
        checklist.append('')
    return checklist
