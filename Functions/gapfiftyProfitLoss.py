from Helpers import extractors
from Helpers import objectConstructors

def gapfiftyprofitlosscalculator(gapfiftyopenpos, gapfiftyidentifyer, gapopenvalue, stoplossvalue, takeprofitvalue, stoplosstr, takeprofitstr, datelistdf2, halvegapvalue, halvehitpos, gapfiftytptime, gapFiftyOpenTime, halveHitTimeStr, gapfiftystoplosstimestrings):
    # I am leaving Capital letter warnings
    # Re-coding will take to long and it does not effect outcome
    count = 0
    myBool = False
    stopLossPosList = []
    forCheckTP = []
    forCheckTP2 = []
    forCheckMom = []
    gapfiftyprofitloss = []
    gapfiftytradeobjectlist = []
    print(' GAPFIFTY  profit loss calculator call received')
    for items in gapfiftyopenpos:
        if gapfiftyidentifyer[count] == 'GAPFIFTY':
            #
            # R-Value
            #
            openvalue = gapopenvalue[count]
            sl = stoplossvalue[count]
            stoplossSize = openvalue - sl
            if stoplossSize < 0:
                stoplossSize = stoplossSize * -1
            # only have gapfifty take profit values for instances where price goes to that value
            if takeprofitvalue[count] != 'NONE':
                takeProfitSize = openvalue - takeprofitvalue[count]
            if takeProfitSize < 0:
                takeProfitSize = takeProfitSize * -1
            Rvalue = (takeProfitSize / stoplossSize)
            #
            # Algo
            #
            # in this case we check the new Stop Loss position string
            # this list carries NONE values for those instances where price does not go through SL
            halveString = stoplosstr[count]
            if halveString != 'NONE':
                forCheckMom = extractors.stringpositionextractor(halveString)
                for positions in forCheckMom:
                    # So i check if there is cases where price goes through sl value after trade is opened
                    # this means there is a chance for stop loss
                    if positions > items:
                        posL = True
                        stopLossPosList.append(positions)
                        # now i have a list that either contains the positions of going through stop loss or NONE if price
                        # did not go through stop loss
                #         so if there is a position where price went through sl then we can say there is a chance for SL
            if posL:
                # here we now know that there is in fact a value for SL
                # we now check if there is a value for TP
                if takeprofitstr[count] != 'NONE':
                    forCheckTP = extractors.stringpositionextractor(takeprofitstr[count])
                    # first i check if there are values for take profit after trade open position
                    for positions in forCheckTP:
                        if positions > items:
                            posTP = True
                            forCheckTP2.append(positions)
                else:
                    #
                    #  BLOK1
                    #
                    # We have no value for take profit but plenty values for sl
                    halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                    halvehittime = halvehittimelist[0]
                    gapfiftyprofitloss.append('LOSS')
                    gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 1.0','gapfifty',
                                                                                  datelistdf2[count],
                                                                                  'LOSS',
                                                                                  0,
                                                                                  halvegapvalue[count],
                                                                                  halvehitpos[count],
                                                                                  gapopenvalue[count],
                                                                                  gapfiftyopenpos[count],
                                                                                  stoplossvalue[count],
                                                                                  takeprofitvalue[count],
                                                                                  stopLossPosList[0],
                                                                                  'NONE',
                                                                                  gapfiftytptime[count],
                                                                                  gapFiftyOpenTime[count],
                                                                                  halvehittime,
                                                                                  gapfiftystoplosstimestrings[count],
                                                                                  ' We have no value for take profit but plenty values for sl')
                    myBool = True
                    gapfiftytradeobjectlist.append(gapfiftyTradeObject)
                    # here i kno that there no value for TP but there is for SL
                if posTP:
                    # this can only be true if there was a value for str
                    if stopLossPosList[0] < forCheckTP2[0]:
                        #
                        #  BLOK 2
                        #
                        gapfiftyprofitloss.append('LOSS')
                        myBool = True
                        halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                        halvehittime = halvehittimelist[0]
                        gapfiftyprofitloss.append('LOSS')
                        gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 2.0','gapfifty', datelistdf2[count], 'LOSS',
                                                                                      0, halvegapvalue[count],
                                                                                      halvehitpos[count],
                                                                                      gapopenvalue[count],
                                                                                      gapfiftyopenpos[count],
                                                                                      stoplossvalue[count],
                                                                                      takeprofitvalue[count],
                                                                                      stopLossPosList[0],
                                                                                      forCheckTP2[0],
                                                                                      gapfiftytptime[count],
                                                                                      gapFiftyOpenTime[count],
                                                                                      halvehittime,
                                                                                      gapfiftystoplosstimestrings[
                                                                                          count],'Stop loss position is < than Take profit position')
                        gapfiftytradeobjectlist.append(gapfiftyTradeObject)
                    if stopLossPosList[0] > forCheckTP2[0]:
                        #
                        # BLOK 3
                        #
                        AP = ('profit', Rvalue)
                        gapfiftyprofitloss.append(AP)
                        myBool = True
                        halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                        halvehittime = halvehittimelist[0]
                        gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 3.0','gapfifty', datelistdf2[count], 'profit',
                                                                                      Rvalue, halvegapvalue[count],
                                                                                      halvehitpos[count],
                                                                                      gapopenvalue[count],
                                                                                      gapfiftyopenpos[count],
                                                                                      stoplossvalue[count],
                                                                                      takeprofitvalue[count],
                                                                                      stopLossPosList[0], forCheckTP2[0],
                                                                                      gapfiftytptime[count],
                                                                                      gapFiftyOpenTime[count],
                                                                                      halvehittime,
                                                                                      gapfiftystoplosstimestrings[
                                                                                          count],'Take profit position is < than stop loss position')
                        gapfiftytradeobjectlist.append(gapfiftyTradeObject)
                    if stopLossPosList[0] == forCheckTP2[0]:
                        #
                        # BLOK 4. simtrade is when tp and sl is triggered in same candle
                        #
                        gapfiftyprofitloss.append('SIM')
                        halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                        halvehittime = halvehittimelist[0]
                        gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 4.0','gapfifty', datelistdf2[count], 'SIM',
                                                                                      0, halvegapvalue[count],
                                                                                      halvehitpos[count],
                                                                                      gapopenvalue[count],
                                                                                      gapfiftyopenpos[count],
                                                                                      stoplossvalue[count],
                                                                                      takeprofitvalue[count],
                                                                                      stopLossPosList[0], forCheckTP2[0],
                                                                                      gapfiftytptime[count],
                                                                                      gapFiftyOpenTime[count],
                                                                                      halvehittime,
                                                                                      gapfiftystoplosstimestrings[
                                                                                          count],' simtrade is when tp and sl is triggered in same candle')
                        gapfiftytradeobjectlist.append(gapfiftyTradeObject)
                else:
                    # if TakeProfitstr was NONE
                    # here we had two ittereations of what could have happened:
                    # 1) there was a NONE value for reverseTakeProfitStr so our check bolean could not go to true
                    # 2) or there was a value for above but no TP values for before trade opened.
                    # Both of these results in this section being activated
                    if takeprofitstr[count] != 'NONE':
                        # SPECIAL Loss Straight Drive (GAPFIFTY) Trade where price reached TP before open and lost after
                        gapfiftyprofitloss.append('LOSS')
                        myBool = True
                        halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                        halvehittime = halvehittimelist[0]
                        gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 5.0','gapfifty', datelistdf2[count], 'LOSS',
                                                                                      0, halvegapvalue[count],
                                                                                      halvehitpos[count],
                                                                                      gapopenvalue[count],
                                                                                      gapfiftyopenpos[count],
                                                                                      stoplossvalue[count],
                                                                                      takeprofitvalue[count],
                                                                                      stoplosstr[count],
                                                                                      takeprofitstr[count],
                                                                                      gapfiftytptime[count],
                                                                                      gapFiftyOpenTime[count],
                                                                                      halvehittime,
                                                                                      gapfiftystoplosstimestrings[
                                                                                          count],'Trade where price reached TP before open and lost after')
                        gapfiftytradeobjectlist.append(gapfiftyTradeObject)
            else:
                # now we kno there no value for SL but there might be a value for TP
                # check if there is a value for reverseTakeProfitstr
                # none value is assigned for instances where price never goes through TP
                if takeprofitstr[count] != 'NONE':
                    forCheckTP = extractors.stringpositionextractor(takeprofitstr[count])
                    # first i check if there are values for take profit after trade open position
                    for positions in forCheckTP:
                        if positions > items:
                            posTP = True
                            forCheckTP2.append(positions)
                    if posTP:
                        # now we know there is no value for sl and a value for tp
                        #
                        # BLOK 6
                        #
                        AP = ('profit', Rvalue)
                        gapfiftyprofitloss.append(AP)
                        myBool = True
                        halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                        halvehittime = halvehittimelist[0]
                        gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 6.0','gapfifty', datelistdf2[count], 'profit',
                                                                                      Rvalue, halvegapvalue[count],
                                                                                      halvehitpos[count],
                                                                                      gapopenvalue[count],
                                                                                      gapfiftyopenpos[count],
                                                                                      stoplossvalue[count],
                                                                                      takeprofitvalue[count],
                                                                                      stoplosstr[count],
                                                                                      forCheckTP2[0],
                                                                                      gapfiftytptime[count],
                                                                                      gapFiftyOpenTime[count],
                                                                                      halvehittime,
                                                                                      gapfiftystoplosstimestrings[
                                                                                          count],
                                                                                      'there is no value for sl and a value for tp')
                        gapfiftytradeobjectlist.append(gapfiftyTradeObject)
                    else:
                        # here we say there is no value for SL
                        # and no value for TP
                        #
                        # Blok 7
                        #
                        gapfiftyprofitloss.append('UNDETERMINED')
                        myBool = True
                        halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                        halvehittime = halvehittimelist[0]
                        gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 7.0','gapfifty', datelistdf2[count], 'UNDETERMINED',
                                                                                      Rvalue, halvegapvalue[count],
                                                                                      halvehitpos[count],
                                                                                      gapopenvalue[count],
                                                                                      gapfiftyopenpos[count],
                                                                                      stoplossvalue[count],
                                                                                      takeprofitvalue[count],
                                                                                      stoplosstr[count],
                                                                                      takeprofitstr[count],
                                                                                      gapfiftytptime[count],
                                                                                      gapFiftyOpenTime[count],
                                                                                      halvehittime,
                                                                                      gapfiftystoplosstimestrings[
                                                                                          count],
                                                                                      'No values for tp and sl')
                        gapfiftytradeobjectlist.append(gapfiftyTradeObject)
                else:
                    #
                    # Blok 8
                    #
                    gapfiftyprofitloss.append('UNDETERMINED')
                    myBool = True
                    halvehittimelist = extractors.stringdtimextractor(halveHitTimeStr[count])
                    halvehittime = halvehittimelist[0]
                    gapfiftyTradeObject = objectConstructors.gapfiftyTradeObjects('Block 8.0','gapfifty', datelistdf2[count],
                                                                                  'UNDETERMINED',
                                                                                  Rvalue, halvegapvalue[count],
                                                                                  halvehitpos[count],
                                                                                  gapopenvalue[count],
                                                                                  gapfiftyopenpos[count],
                                                                                  stoplossvalue[count],
                                                                                  takeprofitvalue[count],
                                                                                  stoplosstr[count],
                                                                                  takeprofitstr[count],
                                                                                  gapfiftytptime[count],
                                                                                  gapFiftyOpenTime[count],
                                                                                  halvehittime,
                                                                                  gapfiftystoplosstimestrings[
                                                                                      count],
                                                                                  'No values for tp and sl')
                    gapfiftytradeobjectlist.append(gapfiftyTradeObject)
        else:
            gapfiftyprofitloss.append('NONE')
            gapfiftytradeobjectlist.append('NONE')
            myBool = True
        stopLossPosList.clear()
        forCheckTP.clear()
        forCheckTP2.clear()
        forCheckMom.clear()
        myBool = False
        loss = False
        posL = False
        posTP = False
        count = count + 1
        mistake = 0
        mistakestr = ''
    return gapfiftytradeobjectlist,gapfiftyprofitloss
