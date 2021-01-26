# Calculates global variable values based on data

def setPipValues(pair):
    rangeHigh = 1407
    testval = pair[3:]
    if testval == 'JPY':
        stoploss = 0.15
        negativegapsizesetnumber = -0.15
        gapsizesetnumber = 0.15
    else:
        stoploss = 0.0015
        negativegapsizesetnumber = -0.0015
        gapsizesetnumber = 0.0015
    return stoploss, negativegapsizesetnumber,gapsizesetnumber, rangeHigh

def stopLists(low, high):
    stoplow = len(low)
    stophigh = len(high)
    return stoplow, stophigh