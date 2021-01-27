# Calculates global variable values based on data

def setPipValues(pair):
    checksetUS = False
    rangeHigh = 1407
    if pair == 'US3030' or pair == 'DE3030':
        stoploss = 15
        negativegapsizesetnumber = -15
        gapsizesetnumber = 15
        checkSetUS = True

    if not checkSetUS:
        testval = pair[3:]
        if testval == 'JPY':
            stoploss = 0.15
            negativegapsizesetnumber = -0.15
            gapsizesetnumber = 0.15
        else:
            stoploss = 0.0015
            negativegapsizesetnumber = -0.0015
            gapsizesetnumber = 0.0015
    return stoploss, negativegapsizesetnumber, gapsizesetnumber, rangeHigh

def stopLists(low, high):
    stoplow = len(low)
    stophigh = len(high)
    return stoplow, stophigh

def ftowopenpip(pair):
    checksetUs = False
    if pair == 'US3030' or pair == 'DE3030':
        setpipvalue = 0.0005
        checkSetUS = True
    if not checkSetUS:
        testval = pair[3:]
        if testval == 'JPY':
            setpipval = 0.15
        else:
            setpipval = 0.0015
        return setpipval

