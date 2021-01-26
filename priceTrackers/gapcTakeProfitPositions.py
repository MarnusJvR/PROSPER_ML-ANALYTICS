def gapctakeprofitposcalculator(gapclasslist,gapsizelist,gapctakeprofitvalue,rangehigh,stopnumber,low,high,mytime):
    forgaplist = []
    takeprofitpos = []
    takeprofitposstr = []
    timetracker = []
    timetrackerstr = []
    tptime = []
    counter = 0
    for gaps in gapclasslist:
        gapsizeCheck = gapsizelist[counter]
        reverseTP = gapctakeprofitvalue[counter]
        if gaps == 'GAP':
            if gapsizeCheck > 0:
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if high[counter + i] >= reverseTP:
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    takeprofitpos.append('NONE')
                    takeprofitposstr.append('NONE')
                    tptime.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    mynum2 = timetracker[0]
                    tptime.append(mynum2)
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    takeprofitposstr.append(reverseSting)
                    takeprofitpos.append(mynum)
            if gapsizeCheck < 0:
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if low[counter + i] <= reverseTP:
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    takeprofitpos.append('NONE')
                    takeprofitposstr.append('NONE')
                    tptime.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    mynum2 = timetracker[0]
                    tptime.append(mynum2)
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    takeprofitposstr.append(reverseSting)
                    takeprofitpos.append(mynum)
        else:
            takeprofitpos.append('NONE')
            takeprofitposstr.append('NONE')
            tptime.append('NONE')
            timetrackerstr.append('NONE')
        gapB = False
        counter = counter + 1
        forgaplist.clear()
        timetracker.clear()
        mynum = 0
    return takeprofitpos,takeprofitposstr,tptime,timetrackerstr
