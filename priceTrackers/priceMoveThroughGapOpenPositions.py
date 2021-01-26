def priceTrackGapOpening(gapclass,gapsizelist,openlistdf2,halvehit,rangehigh,stopnumber,low,high,mytime):
    print('price move back through open calculator')
    priceItem = ()
    gapC = False
    gapB = False
    pricemoveopenposition = []
    forgaplist = []
    timetracker = []
    timetrackerstr = []
    gapfiftyopentime = []
    gapfiftyopenpos = []
    counter = 0
    # I have added the list of values that we go through open here
    for gaps in gapclass:
        gapsizeCheck = gapsizelist[counter]
        myOpenNumber = (float(openlistdf2[counter]))
        if gaps == 'GAP':
            # Only check for price moving through open after hitting 50% gap value
            if halvehit != 'NONE':
                if gapsizeCheck > 0:
                    for i in range(0, rangehigh):
                        if counter + i < stopnumber:
                            if high[counter + i] >= myOpenNumber:
                                forgaplist.append(i)
                                time = mytime[counter + i]
                                timetracker.append(time)
                                gapB = True
                    if not gapB:
                        pricemoveopenposition.append('NONE')
                        gapfiftyopentime.append('NONE')
                        timetrackerstr.append('NONE')
                        gapfiftyopenpos.append('NONE')
                    else:
                        mynum = forgaplist[0]
                        gapfiftyopenpos.append(mynum)
                        mynum2 = timetracker[0]
                        gapfiftyopentime.append(mynum2)
                        timestr = ''
                        for numbers in timetracker:
                            timestr = timestr + str(numbers) + ','
                        timetrackerstr.append(timestr)
                        runStr = ''
                        for items in forgaplist:
                            runStr = runStr + str(items) + ','
                        pricemoveopenposition.append(runStr)
                if gapsizeCheck < 0:
                    for i in range(0, rangehigh):
                        if counter + i < stopnumber:
                            if low[counter + i] <= myOpenNumber:
                                forgaplist.append(i)
                                time = mytime[counter + i]
                                timetracker.append(time)
                                gapB = True
                    if not gapB:
                        pricemoveopenposition.append('NONE')
                        gapfiftyopentime.append('NONE')
                        timetrackerstr.append('NONE')
                        gapfiftyopenpos.append('NONE')
                    else:
                        mynum = forgaplist[0]
                        gapfiftyopenpos.append(mynum)
                        mynum2 = timetracker[0]
                        gapfiftyopentime.append(mynum2)
                        timestr = ''
                        for numbers in timetracker:
                            timestr = timestr + str(numbers) + ','
                        timetrackerstr.append(timestr)
                        runStr = ''
                        for items in forgaplist:
                            runStr = runStr + str(items) + ','
                        pricemoveopenposition.append(runStr)
            else:
                pricemoveopenposition.append('NONE')
                gapfiftyopenpos.append('NONE')
                gapfiftyopentime.append('NONE')
                timetrackerstr.append('NONE')
        else:
            pricemoveopenposition.append('NONE')
            gapfiftyopenpos.append('NONE')
            gapfiftyopentime.append('NONE')
            timetrackerstr.append('NONE')
        gapB = False
        counter = counter + 1
        forgaplist.clear()
        timetracker.clear()
        mynum = 0
    return gapfiftyopenpos,pricemoveopenposition,gapfiftyopentime,timetrackerstr