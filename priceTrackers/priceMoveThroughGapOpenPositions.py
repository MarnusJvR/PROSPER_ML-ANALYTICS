def priceTrackGapOpening(gapclass,gapsizelist,openlistdf2,halvehit,rangehigh,stopnumber,low,high,mytime, halvehitposition):
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
    checknumberlist = []
    openposcheck = False
    opentimetracker = []
    opentimecheck = False
    # I have added the list of values that we go through open here
    # To determine open pos it is important to have those positions after going to 50%
    for gaps in gapclass:
        gapsizeCheck = gapsizelist[counter]
        myOpenNumber = (float(openlistdf2[counter]))
        if gaps == 'GAP':
            # Only check for price moving through open after hitting 50% gap value
            if halvehit[counter] != 'NONE':
                if gapsizeCheck > 0:
                    for i in range(0, rangehigh):
                        if counter + i < stopnumber:
                            if high[counter + i] >= myOpenNumber:
                                forgaplist.append(i)
                                halvehitpos = halvehitposition[counter]
                                if i > halvehitpos:
                                    opentimes = mytime[counter + i]
                                    opentimetracker.append(opentimes)
                                    opentimecheck = True
                                time = mytime[counter + i]
                                timetracker.append(time)
                                gapB = True
                    if not gapB:
                        pricemoveopenposition.append('NONE')
                        gapfiftyopentime.append('NONE')
                        timetrackerstr.append('NONE')
                        gapfiftyopenpos.append('NONE')
                    else:
                        if opentimecheck:
                            mynum2 = opentimetracker[0]
                            gapfiftyopentime.append(mynum2)
                        else:
                            gapfiftyopentime.append('NONE')
                        halvehitpos = halvehitposition[counter]
                        for positions in forgaplist:
                            if positions > halvehitpos:
                                openposcheck = True
                                checknumberlist.append(positions)
                        if openposcheck:
                            mynum = checknumberlist[0]
                            gapfiftyopenpos.append(mynum)
                        else:
                            gapfiftyopenpos.append('NONE')
                        timestr = ''
                        for numbers in timetracker:
                            timestr = timestr + str(numbers) + ','
                        timetrackerstr.append(timestr)
                        runStr = ''
                        for items in checknumberlist:
                            runStr = runStr + str(items) + ','
                        pricemoveopenposition.append(runStr)
                if gapsizeCheck < 0:
                    for i in range(0, rangehigh):
                        if counter + i < stopnumber:
                            if low[counter + i] <= myOpenNumber:
                                forgaplist.append(i)
                                halvehitpos = halvehitposition[counter]
                                if i > halvehitpos:
                                    opentimes = mytime[counter + i]
                                    opentimetracker.append(opentimes)
                                    opentimecheck = True
                                time = mytime[counter + i]
                                timetracker.append(time)
                                gapB = True
                    if not gapB:
                        pricemoveopenposition.append('NONE')
                        gapfiftyopentime.append('NONE')
                        timetrackerstr.append('NONE')
                        gapfiftyopenpos.append('NONE')
                    else:
                        if opentimecheck:
                            mynum2 = opentimetracker[0]
                            gapfiftyopentime.append(mynum2)
                        else:
                            gapfiftyopentime.append('NONE')
                        halvehitpos = halvehitposition[counter]
                        for positions in forgaplist:
                            if positions > halvehitpos:
                                openposcheck = True
                                checknumberlist.append(positions)
                        if openposcheck:
                            mynum = checknumberlist[0]
                            gapfiftyopenpos.append(mynum)
                        else:
                            gapfiftyopenpos.append('NONE')
                        timestr = ''
                        for numbers in timetracker:
                            timestr = timestr + str(numbers) + ','
                        timetrackerstr.append(timestr)
                        runStr = ''
                        for items in checknumberlist:
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
        opentimetracker.clear()
        checknumberlist.clear()
        mynum = 0
        openposcheck = False
        opentimecheck = False
    return gapfiftyopenpos,pricemoveopenposition,gapfiftyopentime,timetrackerstr