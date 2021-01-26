# STOPLOSS PRICE TRACKER
# Function takes the stop loss values of either GAPC or GAPFIFTY and produces positions where price went through SL
# GAPC and GAPFIFY directions of SL is the same for positive and negative gaps

def checkStopLossPositions(gapclasslist, gapsizelist, rangehigh, stoplist, low, high, stopLossImport, mytime):
    # stopLossImport must contain a list of actual price values
    # Stoploss is the same direction for GAPC and GAPFIFTY
    print('stoploss positions calculator call recieved')
    counter = 0
    customstopstr = []
    timetracker = []
    timetrackerstr = []
    gapB = False
    forgaplist = []
    for gaps in gapclasslist:
        gapsizeCheck = gapsizelist[counter]
        if gaps == 'GAP':
            if gapsizeCheck > 0:
                for i in range(0, rangehigh):
                    if counter + i < stoplist:
                        if low[counter + i] <= (stopLossImport[counter]):
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    customstopstr.append('NONE')
                    timetrackerstr.append(('NONE'))
                else:
                    timestr = ''
                    for timestrings in timetracker:
                        timestr = timestr + timestrings + ','
                    timetrackerstr.append(timestr)
                    buildstring = ''
                    for numbers in forgaplist:
                        buildstring = buildstring + str(numbers) + ','
                    customstopstr.append(buildstring)
            if gapsizeCheck < 0:
                for i in range(0, rangehigh):
                    if counter + i < stoplist:
                        if high[counter + i] >= (stopLossImport[counter]):
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    customstopstr.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    timestr = ''
                    for timestrings in timetracker:
                        timestr = timestr + timestrings + ','
                    timetrackerstr.append(timestr)
                    buildstring = ''
                    for numbers in forgaplist:
                        buildstring = buildstring + str(numbers) + ','
                    customstopstr.append(buildstring)
        else:
            customstopstr.append('NONE')
            timetrackerstr.append('NONE')
        gapB = False
        counter = counter + 1
        forgaplist.clear()
        mynum = 0
    return customstopstr, timetrackerstr