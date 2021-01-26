def gapfiftytpcalculator(gapclasslist,gapsizelist,openlistdf,rangehigh,stopnumber,low,high,mytime, gapfiftyopenpos):
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
    opentimetracker = []
    opentimebool = False
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
                            openpos = gapfiftyopenpos[counter]
                            if openpos != 'NONE':
                                if i > openpos:
                                    opentime = mytime[counter + i]
                                    opentimetracker.append(opentime)
                                    opentimebool = True
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
                    if opentimebool:
                        mynum2 = opentimetracker[0]
                        gapfiftytptime.append(mynum2)
                    else:
                        gapfiftytptime.append('NONE')
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    gapfiftytpstr.append(reverseSting)
                    mynum = forgaplist[0]
                    gapfiftytp.append(mynum)
                    gapfiftytpvalue.append(reverseTP)
            if gapsizeCheck < 0:
                reverseTP = float(openlistdf[counter]) + gapsizeCheck
                for i in range(0, rangehigh):
                    if counter + i < stopnumber:
                        if low[counter + i] <= reverseTP:
                            forgaplist.append(i)
                            openpos = gapfiftyopenpos[counter]
                            forgaplist.append(i)
                            openpos = gapfiftyopenpos[counter]
                            if openpos != 'NONE':
                                if i > openpos:
                                    opentime = mytime[counter + i]
                                    opentimetracker.append(opentime)
                                    opentimebool = True
                            time = mytime[counter + i]
                            timetracker.append(time)
                            gapB = True
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
                    if opentimebool:
                        mynum2 = opentimetracker[0]
                        gapfiftytptime.append(mynum2)
                    else:
                        gapfiftytptime.append('NONE')
                    timestr = ''
                    for numbers in timetracker:
                        timestr = timestr + str(numbers) + ','
                    timetrackerstr.append(timestr)
                    reverseSting = ''
                    for numbers in forgaplist:
                        reverseSting = reverseSting + str(numbers) + ','
                    gapfiftytpstr.append(reverseSting)
                    mynum = forgaplist[0]
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
        opentimetracker.clear()
        opentimebool = False
        mynum = 0
    return gapfiftytp,gapfiftytpstr,gapfiftytpvalue,gapfiftytptime,timetrackerstr