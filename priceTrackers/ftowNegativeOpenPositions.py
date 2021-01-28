def ftownegativeopenpositionscalc(mydate,
                                  relevantpricevaluelist,
                                  rangehigh,
                                  stopnumber,
                                  low,
                                  mytime):
    print('ftow negative open position calculator call recieved')
    HitPosStr = []
    hit = []
    hitpos = []
    hittimestr = []
    hitime = []
    forgaplist = []
    timetracker = []
    gapB = False
    counter = 0
    for dates in mydate:
        # Monday= 0 Tuesday = 1 Wednesday = 2 Thursday = 3 Friday = 4
        # We want closing on 4 ! opening on 0 ? !
        weekday = dates.weekday()
        if weekday == 0:
            relevantpricevalue = relevantpricevaluelist[counter]
            for i in range(0, rangehigh):
                if counter + i < stopnumber:
                    if low[counter + i] <= relevantpricevalue:
                        time = mytime[counter + i]
                        timetracker.append(time)
                        forgaplist.append(i)
                        gapB = True
            if not gapB:
                hit.append('NONE')
                hitpos.append('NONE')
                hittimestr.append('NONE')
                HitPosStr.append('NONE')
                hitime.append('NONE')
            else:
                mynum = forgaplist[0]
                hitpos.append(mynum)
                mynum2 = timetracker[0]
                hitime.append(mynum2)
                timestr = ''
                for timestrings in timetracker:
                    timestr = timestr + timestrings + ','
                hittimestr.append(timestr)
                halveStr = ''
                for numbers in forgaplist:
                    halveStr = halveStr + str(numbers) + ','
                HitPosStr.append(halveStr)
                hit.append('HIT')
        else:
            hit.append('NONE')
            hitpos.append('NONE')
            hittimestr.append('NONE')
            HitPosStr.append('NONE')
            hitime.append('NONE')
        gapB = False
        counter = counter + 1
        total = 417336
        perc = counter / total * 100
        print('Loading Negative Open Positions........' + str(perc) + '%')
        forgaplist.clear()
        timetracker.clear()
        mynum = 0
    return hit,hitpos,hittimestr,HitPosStr,hitime








