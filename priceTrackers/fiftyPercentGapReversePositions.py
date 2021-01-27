def fiftypercentpositionreverse(gapclasslist,gapsizelist,halvevaluelist,gapclosenum,rangehigh,stopnumber,low,high,mytime):
    # Calculates the reverse price movement through 50% value
    print('fifty percent gap position in reverse calulator call recieved')
    reversehalvehitposstr = []
    forgaplist = []
    gapcopenpos = []
    reversehalvehit = []
    timetracker = []
    halvehittimestr = []
    gapcopentime = []
    lastPos = 0
    firstPos = []
    firstpostime = []
    gapC = False
    counter = 0
    for gaps in gapclasslist:
        if gaps == 'GAP':
            # I actually need to check those instance that close the gap
            if gapclosenum[counter] != 'NONE':
                # if it hits i check the opposite end to see if it goes back through
                gapsizecheck = gapsizelist[counter]
                halveValue = halvevaluelist[counter]
                if gapsizecheck > 0:
                    for i in range(0, rangehigh):
                        # I check High instead of low
                        if counter + i < stopnumber:
                            if high[counter + i] >= halveValue:
                                time = mytime[counter + i]
                                timetracker.append(time)
                                forgaplist.append(i)
                                gapB = True
                    if not gapB:
                        reversehalvehit.append('NONE')
                        gapcopentime.append('NONE')
                        reversehalvehitposstr.append('NONE')
                        gapcopenpos.append('NONE')
                        halvehittimestr.append('NONE')
                    else:
                        #
                        # I only want to add the position after the gap is closed
                        #
                        lastPos = gapclosenum[counter]
                        halveStr = ''
                        timestr = ''
                        count = 0
                        for numbers in forgaplist:
                            if numbers > lastPos:
                                timeitem = timetracker[count]
                                timestr = timestr + timetracker[count] + ','
                                halveStr = halveStr + str(numbers) + ','
                                gapC = True
                                firstPos.append(numbers)
                                firstpostime.append(timeitem)
                            count = count + 1
                        if halveStr == '':
                            reversehalvehitposstr.append('NONE')
                            halvehittimestr.append('NONE')
                        else:
                            reversehalvehitposstr.append(halveStr)
                            halvehittimestr.append(timestr)
                        if gapC:
                            gapcopenpos.append(firstPos[0])
                            gapcopentime.append(firstpostime[0])
                        else:
                            gapcopenpos.append('NONE')
                            gapcopentime.append('NONE')
                        reversehalvehit.append('HIT')
                if gapsizecheck < 0:
                    for i in range(0, rangehigh):
                        # I check Low instead of High
                        if counter + i < stopnumber:
                            if low[counter + i] <= halveValue:
                                time = mytime[counter + i]
                                timetracker.append(time)
                                forgaplist.append(i)
                                gapB = True
                    if not gapB:
                        reversehalvehit.append('NONE')
                        reversehalvehitposstr.append('NONE')
                        gapcopenpos.append('NONE')
                        halvehittimestr.append('NONE')
                        gapcopentime.append('NONE')
                    else:
                        #
                        # I only want to add the position after the original position crossing 50%
                        #
                        lastPos = gapclosenum[counter]
                        halveStr = ''
                        timestr = ''
                        count = 0
                        for numbers in forgaplist:
                            if numbers > lastPos:
                                timeitem = timetracker[count]
                                timestr = timestr + timetracker[count] + ','
                                halveStr = halveStr + str(numbers) + ','
                                gapC = True
                                firstPos.append(numbers)
                                firstpostime.append(timeitem)
                            count = count + 1
                        if halveStr == '':
                            reversehalvehitposstr.append('NONE')
                            halvehittimestr.append('NONE')
                        else:
                            reversehalvehitposstr.append(halveStr)
                            halvehittimestr.append(timestr)
                        if gapC:
                            gapcopenpos.append(firstPos[0])
                            gapcopentime.append(firstpostime[0])
                        else:
                            gapcopenpos.append('NONE')
                            gapcopentime.append('NONE')
                        reversehalvehit.append('HIT')
            else:
                reversehalvehit.append('NONE')
                reversehalvehitposstr.append('NONE')
                gapcopenpos.append('NONE')
                halvehittimestr.append('NONE')
                gapcopentime.append('NONE')
        else:
            reversehalvehit.append('NONE')
            reversehalvehitposstr.append('NONE')
            gapcopenpos.append('NONE')
            halvehittimestr.append('NONE')
            gapcopentime.append('NONE')
        gapB = False
        gapC = False
        counter = counter + 1
        forgaplist.clear()
        firstPos.clear()
        timetracker.clear()
        firstpostime.clear()
    return reversehalvehit,reversehalvehitposstr,gapcopenpos,gapcopentime,halvehittimestr