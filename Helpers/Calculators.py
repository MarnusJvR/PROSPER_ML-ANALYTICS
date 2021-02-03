from Helpers import extractors
# gap size calculator
def gapsizecalc(openvalues,prevclosingvalues):
    print('calculator call recieved')
    print('--------------------------------')
    diflist = []
    # gap size is calculated by taking the current opening value and subtracting the prev closing value
    # If the prev closing value was higher than opening number EXPECT NEGATIVE NUMBER
    # If opening is higher than pre closing expect POSITIVE NUMBER
    count = 0
    for num in openvalues:
        newvalue = round((float(num) - float(prevclosingvalues[count])), 10)
        count += 1
        diflist.append(newvalue)
    return diflist

# calculate the amount of gaps
def gapCalculator(gapclass):
    gapcounter = 0
    for gaps in gapclass:
        if gaps == 'GAP':
            gapcounter = gapcounter + 1
    return gapcounter

# Function that will generate stoploss values
# takes trade open value and sl size
def stopLossValues(tradeopenvalue, slsize, gapclasslist, gapsizelist):
    print('Stoploss calculator call recieved')
    stoplossfunc = []
    counter = 0
    stopfunc = 0
    for gaps in gapclasslist:
        gapsizeCheck = gapsizelist[counter]
        if gaps == 'GAP':
            if gapsizeCheck > 0:
                stopfunc = tradeopenvalue[counter] - slsize
                stoplossfunc.append(stopfunc)
            if gapsizeCheck < 0:
                stopfunc = tradeopenvalue[counter] + slsize
                stoplossfunc.append(stopfunc)
        else:
            stoplossfunc.append('NONE')
        counter += 1
    return stoplossfunc

# Calculate 50% gap values
def fiftypercentgapvalue(gapclasslist,openvalue,prevclosingvalue):
    print('halve gap calc called recieved')
    print('--------------------------------')
    halvegapvalue = []
    counter = 0
    for gaps in gapclasslist:
        infoString = ''
        gapsizeCheck = gapclasslist[counter]
        addNum = (float(openvalue[counter]) + float(prevclosingvalue[counter])) / 2
        # movementNumber2 = (openListDF2[counter] - halveGapSize)
        # secondSLnum = (movementNumber2 + stoploss)
        # movementNumberNegative2 = (openListDF2[counter] + halveGapSize)
        # secondSLnumNeg = (movementNumberNegative2 + stoploss)
        if gaps == 'GAP':
            halvegapvalue.append(addNum)
        else:
            halvegapvalue.append('NONE')
        counter = counter + 1
    return halvegapvalue

def gapfiftyidentifyer(gapfiftyopenpos,gapclosenum):
    count = 0
    gapfiftyid = []
    for items in gapfiftyopenpos:
        if items != 'NONE':
            # if there is a value for gapfifty open we need to check the gap closed
            # if the gap closed before returning to open it means we are dealing with a gapc strat
            # if gap closed after it is till a trade but prob just a loss trade
            if gapclosenum[count] == 'NONE':
                gapfiftyid.append('GAPFIFTY')
                # here i am happy to open the trade
            else:
                if gapclosenum[count] > items:
                    gapfiftyid.append('GAPFIFTY')
                else:
                    gapfiftyid.append('NONE')
        else:
            gapfiftyid.append('NONE')
        count = count + 1
    return gapfiftyid

def gapcidentifyer(gapclosenum,reversehalvehit,reversehalvehitposstr,reversehalvehitimestr):
    # This loop checks for the gapc
    # reversehalvehitposstr must contain list of positions
    # check if there is values for reverse 50 AFTER gapclose
    forhalveloop = []
    fortimeloop = []
    gapcid = []
    gapcopenposition = []
    gapcopentime = []
    count = 0
    for items in gapclosenum:
        if items != 'NONE':
            # Now we know the gap closed. now we need to check if it moved down back to 50%
            if reversehalvehit[count] != reversehalvehitposstr[count]:
                print('ERROR')
                print(reversehalvehit[count])
                print(reversehalvehitposstr[count])
            if reversehalvehit[count] != 'NONE':
                halveString = reversehalvehitposstr[count]
                halvetimestring = reversehalvehitimestr[count]
                reversehalvepositions = extractors.stringpositionextractor(halveString)
                timestr = extractors.stringdtimextractor(halvetimestring)
                incount = 0
                for positions in reversehalvepositions:
                    if positions > items:
                        halveboon = True
                        forhalveloop.append(positions)
                        fortimeloop.append(timestr[incount])
                    incount = incount + 1
            if halveboon:
                # there is values where price wentback through fifty after it went to gapclose
                gapcid.append('GAPC')
                openPos = forhalveloop[0]
                opentime = fortimeloop[0]
                gapcopentime.append(opentime)
                gapcopenposition.append(openPos)
            else:
                gapcid.append('NONE')
                gapcopentime.append('NONE')
                gapcopenposition.append('NONE')
        else:
            gapcid.append('NONE')
            gapcopenposition.append('NONE')
            gapcopentime.append('NONE')
        count = count + 1
        forhalveloop.clear()
        fortimeloop.clear()
        halveBoon = False
    return gapcid,gapcopentime,gapcopenposition

def gapctpvaluecalcRvalues(gapclass,gapsize, stoploss,rvalue,halvegapvalue):
    takeprofitvalueR = []
    tp = 0
    count = 0
    for gaps in gapclass:
        if gaps == 'GAP':
            # this is how far away the tp must be from open
            tp = stoploss * rvalue
            if gapsize[count] < 0:
                tp = tp * -1
            takeprofitvalue = halvegapvalue[count] + tp
            takeprofitvalueR.append(takeprofitvalue)
        else:
            takeprofitvalueR.append('NONE')
        count = count + 1
    return takeprofitvalueR



def gapctpvaluecalc(gapclass,gapsizelist,openlistdf2):
    # Calculate the take profit values for GAPC based on 2R return
    # I add gapsize value to gap open value
    # I then devide it by two
    # This give me a full gap size away from open
    takeprofitvalue = []
    tp = 0
    count = 0
    for gaps in gapclass:
        gapsizeCheck = gapsizelist[count]
        if gaps == 'GAP':
            gapctp = openlistdf2[count] + gapsizeCheck
            tp = (openlistdf2[count] + gapctp) / 2
            takeprofitvalue.append(tp)
        else:
            takeprofitvalue.append('NONE')
        count = count + 1
    return takeprofitvalue

def ftow15pointsaboveopen(pair, openlistdf2,ftowopenpip):
    checksetUs = False
    ftowopenvaluelist = []
    if pair == 'US3030' or pair == 'DE3030':
        for openvalues in openlistdf2:
            ftowopenvalue = openvalues + (openvalues * ftowopenpip)
            ftowopenvaluelist.append(ftowopenvalue)
        checksetUs = True
    if not checksetUs:
        for items in openlistdf2:
            ftowopenvalue = items + ftowopenpip
            ftowopenvaluelist.append(ftowopenvalue)
    return ftowopenvaluelist

def ftow15pointsbelowopen(pair, openlistdf2,ftowopenpip):
    checksetUs = False
    ftowopenvaluelist = []
    if pair == 'US3030' or pair == 'DE3030':
        for openvalues in openlistdf2:
            ftowopenvalue = openvalues - (openvalues * ftowopenpip)
            ftowopenvaluelist.append(ftowopenvalue)
        checksetUs = True
    if not checksetUs:
        for items in openlistdf2:
            ftowopenvalue = items + ftowopenpip
            ftowopenvaluelist.append(ftowopenvalue)
    return ftowopenvaluelist

def ftowpositivetakeprofitvalue(pair, openlistdf2, ftowopenpip):
    checksetUs = False
    ftowtpvaluelist = []
    if pair == 'US3030' or pair == 'DE3030':
        for openvalues in openlistdf2:
            ftowtpvalue = openvalues + (3 * (openvalues * ftowopenpip))
            ftowtpvaluelist.append(ftowtpvalue)
        checksetUs = True
    if not checksetUs:
        for items in openlistdf2:
            ftowtpvalue = items + (ftowopenpip*3)
            ftowtpvaluelist.append(ftowtpvalue)
    return ftowtpvalue

def ftownegativetakeprofitvalue(pair, openlistdf2, ftowopenpip):
    checksetUs = False
    ftowtpvaluelist = []
    if pair == 'US3030' or pair == 'DE3030':
        for openvalues in openlistdf2:
            ftowtpvalue = openvalues - (3 * (openvalues * ftowopenpip))
            ftowtpvaluelist.append(ftowtpvalue)
        checksetUs = True
    if not checksetUs:
        for items in openlistdf2:
            ftowtpvalue = items - (ftowopenpip*3)
            ftowtpvaluelist.append(ftowtpvalue)
    return ftowtpvalue