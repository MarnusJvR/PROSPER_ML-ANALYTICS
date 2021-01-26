
# Returns: tradelist -> "gap closed" or "none". gapclosenum -> number of candles fromopen that gap closed. gapclosestr-> str of position where price went through close.
# time -> string of times where gap went through close
def gapClosePositionCalc(gapSizeList, gapclasslist, ranghigh, stopnumberlow, stopnumberhigh, low, high, prevclosing, mytime):
    print('Gap calculator call recieve')
    forgaplist = []
    tradelist = []
    gapclosenum = []
    gapclosenumstr = []
    gapclosetime = []
    timetracker = []
    timetrackerstr = []
    gapb = False
    counter = 0
    for gaps in gapclasslist:
        gapsizeCheck = gapSizeList[counter]
        if gaps == 'GAP':
            if gapsizeCheck > 0:
                for i in range(0, ranghigh):
                    if counter + i < stopnumberlow:
                        if low[counter + i] <= (prevclosing[counter]):
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    gapclosetime.append('NONE')
                    tradelist.append('NONE')
                    gapclosenum.append('NONE')
                    gapclosenumstr.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    mynum2 = timetracker[0]
                    gapclosetime.append(mynum2)
                    gapclosetimestr = ''
                    for numbers in timetracker:
                        gapclosetimestr = gapclosetimestr + str(numbers) + ','
                    timetrackerstr.append(gapclosetimestr)
                    gapCloseStr = ''
                    for numbers in forgaplist:
                        gapCloseStr = gapCloseStr + str(numbers) + ','
                    gapclosenumstr.append(gapCloseStr)
                    tradelist.append('GAP CLOSED')
                    gapclosenum.append(mynum)
            if gapsizeCheck < 0:
                for i in range(0, ranghigh):
                    if counter + i < stopnumberhigh:
                        if high[counter + i] >= (prevclosing[counter]):
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    gapclosetime.append('NONE')
                    tradelist.append('NONE')
                    gapclosenum.append('NONE')
                    gapclosenumstr.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    mynum2 = timetracker[0]
                    gapclosetime.append(mynum2)
                    gapclosetimestr = ''
                    for numbers in timetracker:
                        gapclosetimestr = gapclosetimestr + str(numbers) + ','
                    timetrackerstr.append(gapclosetimestr)
                    gapCloseStr = ''
                    for numbers in forgaplist:
                        gapCloseStr = gapCloseStr + str(numbers) + ','
                    gapclosenumstr.append(gapCloseStr)
                    tradelist.append('GAP CLOSED')
                    gapclosenum.append(mynum)
        else:
            gapclosetime.append('NONE')
            tradelist.append('NONE')
            gapclosenum.append('NONE')
            gapclosenumstr.append('NONE')
            timetrackerstr.append('NONE')
        gapB = False
        counter = counter + 1
        forgaplist.clear()
        mynum = 0
        timetracker.clear()
    return tradelist, gapclosenum, gapclosenumstr, timetrackerstr, gapclosetime

