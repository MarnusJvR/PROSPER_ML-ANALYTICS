from Helpers import extractors
from Helpers import objectConstructors


def gapcprofitlosscalc(gapcopenpos,
                       halvegapvalue,
                       gapcstoplossval,
                       gapctppos,
                       gapctakeprofitvalue,
                       gapcstoplossposstr,
                       gapctakeprofitposstr,
                       datelistdf2,
                       gapclosenum,
                       gapclosepostr,
                       gapclosetime,
                       gapcopentime,
                       takeprofittime,
                       stoplosstime):
    positionsslaftertradeopen = []
    positionsTPaftertradeopen = []
    gapcProfitLoss = []
    gapcTradeObjectList = []
    forCheckTP = []
    stoplosscheck = []
    stoplosscheckrun = []
    stoplosscheckboon = False
    stoplosstimecheck = []
    stoplosstimecheckrun = []
    stoplosstimecheckboon = False
    tpposcheckrun = []
    tpposcheckrunbool = False
    count = 0
    print(' GAPC profit loss calculator call received')

    for items in gapcopenpos:
        if items != 'NONE':
            # if there is an open position gapc trade is true
            opennum = items
            openv = halvegapvalue[count]
            sl = gapcstoplossval[count]
            stoplossSize = openv - sl
            if stoplossSize < 0:
                stoplossSize = stoplossSize * -1
            # only have gapc take profit positions for instances where price goes to that value
            if gapctppos[count] != 'NONE':
                takeProfitSize = openv - gapctakeprofitvalue[count]
            if takeProfitSize < 0:
                takeProfitSize = takeProfitSize * -1
            rvalue = (takeProfitSize / stoplossSize)
            closenum = gapcstoplossposstr[count]
            if closenum != 'NONE':
                forcheckmom = extractors.stringpositionextractor(closenum)
                for positions in forcheckmom:
                    # if there is value for gapclose after trade is opened we have chance for sl
                    if positions > opennum:
                        # in this case there is a chance for stoploss
                        closeboon = True
                        positionsslaftertradeopen.append(positions)
            if closeboon:
                #
                # here we now know that there is in fact a value for SL
                # we now check if there is a value for TP
                #
                if gapctakeprofitposstr[count] != 'NONE':
                    #
                    # Value for SL and TP
                    #
                    # No else block cause the undetermined is caught below
                    forCheckTP = extractors.stringpositionextractor(gapctakeprofitposstr[count])
                    # first i check if there are values for take profit after trade open position
                    for positions in forCheckTP:
                        # check if there is positions for tp after trade is open
                        if positions > opennum:
                            posTP = True
                            positionsTPaftertradeopen.append(positions)
                    if posTP:
                        #
                        #
                        # Values for tp after trade is opened & values for SL
                        #
                        #
                        if positionsslaftertradeopen[0] > positionsTPaftertradeopen[0]:
                            #
                            # Trade went through TP before going through SL
                            #
                            # I first get the value for stoploss time
                            stoplosstimecheck = extractors.stringdtimextractor(stoplosstime[count])
                            increments = 0
                            for timeelements in stoplosstimecheck:
                                if increments == positionsslaftertradeopen[0]:
                                    stoplosstimecheckrun.append(timeelements)
                                    stoplosstimecheckboon = True
                                increments = increments + 1
                            if stoplosstimecheckboon:
                                stoplosstimenafteropen = stoplosstimecheckrun[0]
                            else:
                                stoplosstimenafteropen = 'NONE'
                            AP = ('profit', rvalue)
                            gapcProfitLoss.append(AP)
                            gapcTradeObject = objectConstructors.gapcTradeObjects('Block 1.0',
                                                                                  'GAPC',
                                                                                  datelistdf2[count],
                                                                                  'Profit',
                                                                                  rvalue,
                                                                                  gapclosenum[count],
                                                                                  gapcopenpos[count],
                                                                                  gapctakeprofitvalue[count],
                                                                                  gapcstoplossval[count],
                                                                                  positionsTPaftertradeopen[0],
                                                                                  positionsslaftertradeopen[0],
                                                                                  gapclosetime[count],
                                                                                  gapcopentime[count],
                                                                                  takeprofittime[count],
                                                                                  stoplosstimenafteropen,
                                                                                  'take profit position after trade is opened is < than stop loss position after trade is opened')

                            gapcTradeObjectList.append(gapcTradeObject)
                            myBool = True
                            checkBool = True

                        if positionsslaftertradeopen[0] < positionsTPaftertradeopen[0]:
                            #
                            # SL was was hit before the TP
                            #
                            stoplosstimecheck = extractors.stringdtimextractor(stoplosstime[count])
                            increments = 0
                            for timeelements in stoplosstimecheck:
                                if increments == positionsslaftertradeopen[0]:
                                    stoplosstimecheckrun.append(timeelements)
                                    stoplosstimecheckboon = True
                                increments = increments + 1
                            if stoplosstimecheckboon:
                                stoplosstimenafteropen = stoplosstimecheckrun[0]
                            else:
                                stoplosstimenafteropen = 'NONE'
                            gapcProfitLoss.append('LOSS')
                            gapcTradeObject = objectConstructors.gapcTradeObjects('Block 2.0',
                                                                                  'GAPC',
                                                                                  datelistdf2[count],
                                                                                  'Loss',
                                                                                  0,
                                                                                  gapclosenum[count],
                                                                                  gapcopenpos[count],
                                                                                  gapctakeprofitvalue[count],
                                                                                  gapcstoplossval[count],
                                                                                  positionsTPaftertradeopen[0],
                                                                                  positionsslaftertradeopen[0],
                                                                                  gapclosetime[count],
                                                                                  gapcopentime[count],
                                                                                  takeprofittime[count],
                                                                                  stoplosstimenafteropen,
                                                                                  'stop loss position after trade is opened < take profit position after trade is opened is')
                            gapcTradeObjectList.append(gapcTradeObject)
                            myBool = True
                            checkBool = True
                        if positionsslaftertradeopen[0] == positionsTPaftertradeopen[0]:
                            gapcProfitLoss.append('SIM')
                            stoplosstimecheck = extractors.stringdtimextractor(stoplosstime[count])
                            increments = 0
                            for timeelements in stoplosstimecheck:
                                if increments == positionsslaftertradeopen[0]:
                                    stoplosstimecheckrun.append(timeelements)
                                    stoplosstimecheckboon = True
                                increments = increments + 1
                            if stoplosstimecheckboon:
                                stoplosstimenafteropen = stoplosstimecheckrun[0]
                            else:
                                stoplosstimenafteropen = 'NONE'
                            gapcProfitLoss.append('LOSS')
                            gapcTradeObject = objectConstructors.gapcTradeObjects('Block 3.0',
                                                                                  'GAPC',
                                                                                  datelistdf2[count],
                                                                                  'SIM',
                                                                                  0,
                                                                                  gapclosenum[count],
                                                                                  gapcopenpos[count],
                                                                                  gapctakeprofitvalue[count],
                                                                                  gapcstoplossval[count],
                                                                                  positionsTPaftertradeopen[0],
                                                                                  positionsslaftertradeopen[0],
                                                                                  gapclosetime[count],
                                                                                  gapcopentime[count],
                                                                                  takeprofittime[count],
                                                                                  stoplosstimenafteropen,
                                                                                  'Price hits SL & TP in same candle')
                            gapcTradeObjectList.append(gapcTradeObject)
                            myBool = True
                            checkBool = True
                    else:
                        #
                        # Here there are values for TP and SL but no values for TP AFTER trade open
                        #
                        # The following logic I could add in the beggining of the loop but I find this is easier to
                        # navigate and problem solve I extract stoploss pos for after
                        if gapcstoplossposstr[count] != 'NONE':
                            stoplosscheck = extractors.stringpositionextractor(gapcstoplossposstr[count])
                            for stops in stoplosscheck:
                                if items < stops:
                                    stoplosscheckrun.append(stops)
                                    stoplosscheckboon = True
                            if stoplosscheckboon:
                                stoplosspositionafteropen = stoplosscheckrun[0]
                            else:
                                stoplosspositionafteropen = 'NONE'
                        else:
                            stoplosspositionafteropen = 'NONE'
                        # I extract stoploss time value for after open
                        if stoplosspositionafteropen != 'NONE':
                            stoplosstimecheck = extractors.stringdtimextractor(stoplosstime[count])
                            increments = 0
                            for timeelements in stoplosstimecheck:
                                if increments == stoplosspositionafteropen:
                                    stoplosstimecheckrun.append(timeelements)
                                    stoplosstimecheckboon = True
                                increments = increments + 1
                            if stoplosstimecheckboon:
                                stoplosstimenafteropen = stoplosstimecheckrun[0]
                            else:
                                stoplosstimenafteropen = 'NONE'
                        else:
                            stoplosstimenafteropen = 'NONE'

                        gapcProfitLoss.append('LOSS')
                        gapcTradeObject = objectConstructors.gapcTradeObjects('Block 4.0',
                                                                              'GAPC',
                                                                              datelistdf2[count],
                                                                              'Loss',
                                                                              0,
                                                                              gapclosenum[count],
                                                                              gapcopenpos[count],
                                                                              gapctakeprofitvalue[count],
                                                                              gapcstoplossval[count],
                                                                              gapctakeprofitposstr[count],
                                                                              stoplosspositionafteropen,
                                                                              gapclosetime[count],
                                                                              gapcopentime[count],
                                                                              takeprofittime[count],
                                                                              stoplosstimenafteropen,
                                                                              'Price reaches take profit before opening the trade. The trade is opened, but then goes to stop loss after')
                        gapcTradeObjectList.append(gapcTradeObject)
                else:
                    #
                    #  We have no value for take profit but plenty values for sl. closeboon is true
                    #
                    # I extract stoploss value for after open
                    if gapcstoplossposstr[count] != 'NONE':
                        stoplosscheck = extractors.stringpositionextractor(gapcstoplossposstr[count])
                        for stops in stoplosscheck:
                            if items < stops:
                                stoplosscheckrun.append(stops)
                                stoplosscheckboon = True
                        if stoplosscheckboon:
                            stoplosspositionafteropen = stoplosscheckrun[0]
                        else:
                            stoplosspositionafteropen = 'NONE'
                    else:
                        stoplosspositionafteropen = 'NONE'
                    # I extract stoploss time value for after open
                    if stoplosspositionafteropen != 'NONE':
                        stoplosstimecheck = extractors.stringdtimextractor(stoplosstime[count])
                        increments = 0
                        for timeelements in stoplosstimecheck:
                            if increments == stoplosspositionafteropen:
                                stoplosstimecheckrun.append(timeelements)
                                stoplosstimecheckboon = True
                            increments = increments + 1
                        if stoplosstimecheckboon:
                            stoplosstimenafteropen = stoplosstimecheckrun[0]
                        else:
                            stoplosstimenafteropen = 'NONE'
                    else:
                        stoplosstimenafteropen = 'NONE'

                    gapcProfitLoss.append('LOSS')
                    gapcTradeObject = objectConstructors.gapcTradeObjects('Block 5.0',
                                                                          'GAPC',
                                                                          datelistdf2[count],
                                                                          'Loss',
                                                                          0,
                                                                          gapclosenum[count],
                                                                          gapcopenpos[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossval[count],
                                                                          gapctakeprofitposstr[count],
                                                                          stoplosspositionafteropen,
                                                                          gapclosetime[count],
                                                                          gapcopentime[count],
                                                                          takeprofittime[count],
                                                                          stoplosstimenafteropen,
                                                                          'No take profit values, but plenty of stop loss values')
                    gapcTradeObjectList.append(gapcTradeObject)
                    myBool = True
                    checkBool = True

            else:
                #
                # No value for SL. CHECK fo TP
                # if there is any value for take profit after trade open we are good
                if gapctakeprofitposstr[count] != 'NONE':
                    AP = ('profit', rvalue)
                    # Extract the takeprofit position
                    tpposcheck = extractors.stringpositionextractor(gapctakeprofitposstr[count])
                    for elements in tpposcheck:
                        if elements > opennum:
                            tpposcheckrun.append(elements)
                            tpposcheckrunbool = True
                    if tpposcheckrunbool:
                        tpposition = tpposcheckrun[0]
                    else:
                        tpposition = 'NONE'
                    gapcTradeObject = objectConstructors.gapcTradeObjects('Block 6.0',
                                                                          'GAPC',
                                                                          datelistdf2[count],
                                                                          'Profit',
                                                                          rvalue,
                                                                          gapclosenum[count],
                                                                          gapcopenpos[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossval[count],
                                                                          tpposition,
                                                                          gapcstoplossposstr[count],
                                                                          gapclosetime[count],
                                                                          gapcopentime[count],
                                                                          takeprofittime[count],
                                                                          stoplosstime[count],
                                                                          'No value for stop loss, but there are values for take profit')
                    gapcTradeObjectList.append(gapcTradeObject)
                    gapcProfitLoss.append(AP)
                    myBool = True
                    checkBool = True

                else:
                    #
                    # No value for SL or TP
                    #
                    gapcProfitLoss.append('UNDETERMINED')
                    gapcTradeObject = objectConstructors.gapcTradeObjects('Block 7.0',
                                                                          'GAPC',
                                                                          datelistdf2[count],
                                                                          'Undetermined',
                                                                          rvalue,
                                                                          gapclosenum[count],
                                                                          gapcopenpos[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossval[count],
                                                                          positionsTPaftertradeopen[0],
                                                                          gapcstoplossposstr[count],
                                                                          gapclosetime[count],
                                                                          gapcopentime[count],
                                                                          takeprofittime[count],
                                                                          stoplosstime[count],
                                                                          'No values for stop loss or take profit. Price just dicked around')
                    gapcTradeObjectList.append(gapcTradeObject)
                    myBool = True
                    checkBool = True

        else:
            gapcProfitLoss.append('NONE')
            gapcTradeObjectList.append('NONE')
        count = count + 1
        positionsTPaftertradeopen.clear()
        forCheckTP.clear()
        positionsslaftertradeopen.clear()
        stoplosscheckrun.clear()
        stoplosstimecheckrun.clear()
        tpposcheckrun.clear()
        tpposcheckrunbool = False
        stoplosscheckboon = False
        stoplosstimecheckboon = False
        closeboon = False
        posTP = False
    return gapcProfitLoss, gapcTradeObjectList
