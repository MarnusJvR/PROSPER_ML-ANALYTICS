
print(' GAPCTAKE PROFITVALUE CALCULATOR call received')
def gapctakeprofitposcalculator(gapclasslist,
                                gapsizelist,
                                gapctakeprofitvalue,
                                rangehigh,
                                stopnumber,
                                low,
                                high,
                                mytime,
                                gapcopenpos):
    forgaplist = []
    takeprofitpos = []
    takeprofitposstr = []
    timetracker = []
    timetrackerstr = []
    opentimetracker = []
    opentimebool = False
    tptime = []
    counter = 0
    print(' GAPCTAKEPR OFITVALUE CALCULATOR call received')
    for gaps in gapclasslist:
        gapsizeCheck = gapsizelist[counter]
        reverseTP = gapctakeprofitvalue[counter]
        if gaps == 'GAP':
            if gapsizeCheck > 0:
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if high[counter + i] >= reverseTP:
                            forgaplist.append(i)
                            openpos = gapcopenpos[counter]
                            if openpos != 'NONE':
                                if i > openpos:
                                    opentime = mytime[counter + i]
                                    opentimetracker.append(opentime)
                                    opentimebool = True
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    takeprofitpos.append('NONE')
                    takeprofitposstr.append('NONE')
                    tptime.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    if opentimebool:
                        mynum2 = opentimetracker[0]
                        tptime.append(mynum2)
                    else:
                        tptime.append('NONE')
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    takeprofitposstr.append(reverseSting)
                    mynum = forgaplist[0]
                    takeprofitpos.append(mynum)
            if gapsizeCheck < 0:
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if low[counter + i] <= reverseTP:
                            forgaplist.append(i)
                            if openpos != 'NONE':
                                if i > openpos:
                                    opentime = mytime[counter + i]
                                    opentimetracker.append(opentime)
                                    opentimebool = True
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    takeprofitpos.append('NONE')
                    takeprofitposstr.append('NONE')
                    tptime.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    if opentimebool:
                        mynum2 = opentimetracker[0]
                        tptime.append(mynum2)
                    else:
                        tptime.append('NONE')
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    takeprofitposstr.append(reverseSting)
                    mynum = forgaplist[0]
                    takeprofitpos.append(mynum)
        else:
            takeprofitpos.append('NONE')
            takeprofitposstr.append('NONE')
            tptime.append('NONE')
            timetrackerstr.append('NONE')
        gapB = False
        counter = counter + 1
        opentimebool = False
        opentimetracker.clear()
        forgaplist.clear()
        timetracker.clear()
        mynum = 0
    return takeprofitpos,takeprofitposstr,tptime,timetrackerstr
