# checking if it went back through openvalue for GAPFIFTY
# This checks after it went through halve gap
# position is determined as how many itterations from gap opening it goes through the open value again with parameter that it must first have reached 50

def openpositioncalculator(halvehit):
    # halvehit containing the 'HIT' for all trades going to 50%
    momentumOpenHitPos = []
    forOpenList = []
    momentumO = []
    counter = 0
    for hits in halvehit:
        if hits == 'HIT':
            hhPosition = halveHitPos[counter]
            priceMovestr = priceMoveOpenCount[counter]
            # use extractor to extract values
            forOpenList = extractor(priceMovestr)
            for positions in forOpenList:
                # Important: we only check to open the reverse trade 4 itterations from when the gap opened for market reasons
                # I removed the 4 itteration rule
                if positions > hhPosition:
                    momentumO.append(positions)
            # now i have all the positions where price went back through oppen value after the 50% value was reached
            if len(momentumO) != 0:
                momentumOpenHitPos.append(momentumO[0])
            else:
                momentumOpenHitPos.append('NONE')
        else:
            momentumOpenHitPos.append('NONE')
        forOpenList.clear()
        momentumO.clear()
        counter = counter + 1

    df2['Straight Drive Open Position'] = momentumOpenHitPos


