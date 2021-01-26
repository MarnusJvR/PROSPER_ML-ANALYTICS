from Helpers import extractors
from Helpers import objectConstructors


def gapcprofitlosscalc(gapcopenpos, halvegapvalue, gapcstoplossval, gapctppos, gapctakeprofitvalue, gapcstoplossposstr,
                       gapctakeprofitposstr, datelistdf2, gapclosenum, gapclosepostr, gapclosetime, gapcopentime,
                       takeprofittime, stoplosstime):
    positionsslaftertradeopen = []
    positionsTPaftertradeopen = []
    gapcProfitLoss = []
    gapcTradeObjectList = []
    forCheckTP = []
    count = 0
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
                            AP = ('profit', rvalue)
                            gapcProfitLoss.append(AP)
                            gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC', datelistdf2[count],
                                                                                  'Profit',
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
                                                                                  stoplosstime[count])

                            gapcTradeObjectList.append(gapcTradeObject)
                            myBool = True
                            checkBool = True

                        if positionsslaftertradeopen[0] < positionsTPaftertradeopen[0]:
                            #
                            # SL was was hit before the TP
                            #
                            gapcProfitLoss.append('LOSS')
                            gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC',datelistdf2[count], 'Loss', 0,
                                                                                  gapclosenum[count],
                                                                                  gapcopenpos[count],
                                                                                  gapctakeprofitvalue[count],
                                                                                  gapcstoplossval[count],
                                                                                  positionsTPaftertradeopen[0],
                                                                                  gapcstoplossposstr[count],
                                                                                  gapclosetime[count],
                                                                                  gapcopentime[count],
                                                                                  takeprofittime[count],
                                                                                  stoplosstime[count])
                            gapcTradeObjectList.append(gapcTradeObject)
                            myBool = True
                            checkBool = True
                        if positionsslaftertradeopen[0] == positionsTPaftertradeopen[0]:
                            gapcProfitLoss.append('SIM')
                            gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC',datelistdf2[count],
                                                                                  'SIM (Price hits SL & TP in same candle',
                                                                                  0,
                                                                                  gapclosenum[count],
                                                                                  gapcopenpos[count],
                                                                                  gapctakeprofitvalue[count],
                                                                                  gapcstoplossval[count],
                                                                                  positionsTPaftertradeopen[0],
                                                                                  gapcstoplossposstr[count],
                                                                                  gapclosetime[count],
                                                                                  gapcopentime[count],
                                                                                  takeprofittime[count],
                                                                                  stoplosstime[count])
                            gapcTradeObjectList.append(gapcTradeObject)
                            myBool = True
                            checkBool = True
                    else:
                        #
                        # Here there are values for TP and SL but no values for TP AFTER trade open
                        #
                        gapcProfitLoss.append('LOSS')
                        gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC',datelistdf2[count], 'Loss', 0,
                                                                              gapclosenum[count], gapcopenpos[count],
                                                                              gapctakeprofitvalue[count],
                                                                              gapcstoplossval[count],
                                                                              gapclosepostr[count],
                                                                              gapcstoplossposstr[count],
                                                                              gapclosetime[count],
                                                                              gapcopentime[count],
                                                                              takeprofittime[count],
                                                                              stoplosstime[count])
                        gapcTradeObjectList.append(gapcTradeObject)
                else:
                    #
                    #  We have no value for take profit but plenty values for sl. closeboon is true
                    #
                    # print('-------------')
                    gapcProfitLoss.append('LOSS')
                    gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC',datelistdf2[count], 'Loss', 0,
                                                                          gapclosenum[count], gapcopenpos[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossval[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossposstr[count],
                                                                          gapclosetime[count],
                                                                          gapcopentime[count],
                                                                          takeprofittime[count],
                                                                          stoplosstime[count])
                    gapcTradeObjectList.append(gapcTradeObject)
                    myBool = True
                    checkBool = True

            else:
                #
                # No value for SL. CHECK fo TP
                # if there is any value for take profit after trade open we are good
                if gapctakeprofitposstr[count] != 'NONE':
                    AP = ('profit', rvalue)
                    gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC',datelistdf2[count], 'Profit', rvalue,
                                                                          gapclosenum[count], gapcopenpos[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossval[count],
                                                                          gapctakeprofitposstr[
                                                                              count],
                                                                          gapcstoplossposstr[count],
                                                                          gapclosetime[count],
                                                                          gapcopentime[count],
                                                                          takeprofittime[count],
                                                                          stoplosstime[count])
                    gapcTradeObjectList.append(gapcTradeObject)
                    gapcProfitLoss.append(AP)
                    myBool = True
                    checkBool = True

                else:
                    #
                    # No value for SL or TP
                    #
                    gapcProfitLoss.append('UNDETERMINED')
                    gapcTradeObject = objectConstructors.gapcTradeObjects('GAPC',datelistdf2[count],
                                                                          'Undetermined - Neither SL nor TP reached',
                                                                          rvalue,
                                                                          gapclosenum[count], gapcopenpos[count],
                                                                          gapctakeprofitvalue[count],
                                                                          gapcstoplossval[count],
                                                                          positionsTPaftertradeopen[0],
                                                                          gapcstoplossposstr[count],
                                                                          gapclosetime[count],
                                                                          gapcopentime[count],
                                                                          takeprofittime[count],
                                                                          stoplosstime[count])
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
        closeboon = False
        posTP = False
    return gapcProfitLoss, gapcTradeObjectList
