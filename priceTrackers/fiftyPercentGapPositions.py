def fiftypercentpositions(gapclasslist,gapsizelist,halvegapvalues,rangehigh,stopnumber,low,high,mytime):
    print('GAP fifty percent position calculator call recieved')
    halveHitPosStr = []
    halvehit = []
    halvehitpos = []
    halvehittimestr = []
    forgaplist = []
    timetracker = []

    gapB = False
    counter = 0
    for gaps in gapclasslist:
        if gaps == 'GAP':
            gapsizeCheck = gapsizelist[counter]
            halveValue = halvegapvalues[counter]
            if gapsizeCheck > 0:
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if low[counter + i] <= halveValue:
                            time = mytime[counter + i]
                            timetracker.append(time)
                            forgaplist.append(i)
                            gapB = True
                if not gapB:
                    halvehit.append('NONE')
                    halvehitpos.append('NONE')
                    halvehittimestr.append('NONE')
                    halveHitPosStr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    timestr = ''
                    for timestrings in timetracker:
                        timestr = timestr + timestrings + ','
                    halvehittimestr.append(timestr)
                    halveStr = ''
                    for numbers in forgaplist:
                        halveStr = halveStr + str(numbers) + ','
                    halveHitPosStr.append(halveStr)
                    halvehit.append('HIT')
                    halvehitpos.append(mynum)
            if gapsizeCheck < 0:
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if high[counter + i] >= halveValue:
                            time = mytime[counter + i]
                            timetracker.append(time)
                            forgaplist.append(i)
                            gapB = True
                if not gapB:
                    halvehit.append('NONE')
                    halvehitpos.append('NONE')
                    halvehittimestr.append('NONE')
                    halveHitPosStr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    for timestrings in timetracker:
                        timestr = timestr + timestrings + ','
                    halvehittimestr.append(timestr)
                    halveStr = ''
                    for numbers in forgaplist:
                        halveStr = halveStr + str(numbers) + ','
                    halveHitPosStr.append(halveStr)
                    halvehit.append('HIT')
                    halvehitpos.append(mynum)
        else:
            halvehittimestr.append('NONE')
            halvehit.append('NONE')
            halveHitPosStr.append('NONE')
            halvehitpos.append('NONE')
        gapB = False
        counter = counter + 1
        forgaplist.clear()
        mynum = 0
    return halveHitPosStr,halvehittimestr,halvehit, halvehitpos
