def gapfiftytpcalculator(gapclasslist,gapsizelist,openlistdf,rangehigh,stopnumber,low,high,mytime):
    print(' GAPFIFTY take profit calculator call recieved')
    # GAPFIFTY drive take profit positions
    # price goes to 50% then return to TP
    forgaplist = []
    gapfiftytp = []
    gapfiftytpstr = []
    gapfiftytpvalue = []
    timetracker = []
    timetrackerstr = []
    gapfiftytptime = []
    counter = 0
    for gaps in gapclasslist:
        gapsizeCheck = gapsizelist[counter]
        if gaps == 'GAP':
            if gapsizeCheck > 0:
                reverseTP = openlistdf[counter] + gapsizeCheck
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if high[counter + i] >= reverseTP:
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    gapfiftytp.append('NONE')
                    gapfiftytpstr.append('NONE')
                    gapfiftytpvalue.append('NONE')
                    gapfiftytptime.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    mynum2 = timetracker[0]
                    gapfiftytptime.append(mynum2)
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    gapfiftytpstr.append(reverseSting)
                    gapfiftytp.append(mynum)
                    gapfiftytpvalue.append(reverseTP)
            if gapsizeCheck < 0:
                reverseTP = float(openlistdf[counter]) + gapsizeCheck
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if low[counter + i] <= reverseTP:
                            forgaplist.append(i)
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
                if not gapB:
                    gapfiftytp.append('NONE')
                    gapfiftytpstr.append('NONE')
                    gapfiftytpvalue.append('NONE')
                    gapfiftytptime.append('NONE')
                    timetrackerstr.append('NONE')
                else:
                    mynum = forgaplist[0]
                    mynum2 = timetracker[0]
                    gapfiftytptime.append(mynum2)
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    gapfiftytpstr.append(reverseSting)
                    gapfiftytp.append(mynum)
                    gapfiftytpvalue.append(reverseTP)
        else:
            gapfiftytp.append('NONE')
            gapfiftytpstr.append('NONE')
            gapfiftytpvalue.append('NONE')
            gapfiftytptime.append('NONE')
            timetrackerstr.append('NONE')
        gapB = False
        counter = counter + 1
        forgaplist.clear()
        timetracker.clear()
        mynum = 0
    return gapfiftytp,gapfiftytpstr,gapfiftytpvalue,gapfiftytptime,timetrackerstr