from Helpers import objectConstructors
from Helpers import extractors
def ftowprofitlossCalculator(mydate,
                             ftowid,
                             positiveTPvalue,
                             positiveTPpos,
                             positiveTPtime,
                             positiveOpenvalue,
                             positiveOpenpos,
                             positiveOpentime,
                             positiveSLvalue,
                             positiveSLpos,
                             possitiveSLltime,
                             positiveSLstring,
                             negativeTPvalue,
                             negativeTPpos,
                             negativeTPtime,
                             negativeOpenvalue,
                             negativeOpenpos,
                             negativeOpentime,
                             negativeSLvalue,
                             negativeSLpos,
                             negativeSLltime,
                             negativeSLstring):
    profitloss = []
    ftowTradeObjectList = []
    checkList = []
    checkBool = False
    counter = 0
    print('TOW profit loss calc is running')
    for dates in mydate:
        # Monday= 0 Tuesday = 1 Wednesday = 2 Thursday = 3 Friday = 4
        # We want closing on 4 ! opening on 0 ? !
        weekday = dates.weekday()
        if weekday == 0:
            if ftowid[counter] != 'NONE':
                # If there is a value for Take profit we have to assume that price went through open
                if ftowid[counter] == 'Positive':
                    if positiveTPpos[counter] != 'NONE':
                        # Here we know there are values for Take Profit
                        if positiveSLpos[counter] == 'NONE':
                            # no values for stoploss
                            # 'There is a value for Take profit but no value for Stop loss'
                            # --BLOCK 1.0--
                            profitloss.append('PROFIT')
                            ftowObject = objectConstructors.ftowobjectcreator('BLOCK 1.0',
                                                                              'FTOW',
                                                                              dates,
                                                                              'PROFIT',
                                                                              3,
                                                                              positiveOpenvalue[counter],
                                                                              positiveOpenpos[counter],
                                                                              positiveOpentime[counter],
                                                                              positiveTPvalue[counter],
                                                                              positiveTPpos[counter],
                                                                              positiveTPtime[counter],
                                                                              positiveSLvalue[counter],
                                                                              positiveSLpos[counter],
                                                                              possitiveSLltime[counter],
                                                                              'There is a value for Take profit but no value for Stop loss')
                            ftowTradeObjectList.append(ftowObject)
                        else:
                            # here we have values for both sl and tp
                            # first check for the SL values after trade open
                            stoplossvalues = extractors.stringpositionextractor(positiveSLstring[counter])
                            for items in stoplossvalues:
                                if items > positiveOpenpos:
                                    checkList.append(items)
                                    checkBool = True
                            if checkBool:
                                # Here we know that there are possibility for SL
                                # We now check all the possible itteration
                                # SL > TP. TP > SL. TP == SL
                                SLafterTradeOpenPosition = checkList[0]
                                # Here we now that there are values for SL after trade open
                                if SLafterTradeOpenPosition < positiveTPpos[counter]:
                                    # price went to stop loss after trade open before reaching takeprofit
                                    profitloss.append('LOSS')
                                    ftowObject = objectConstructors.ftowobjectcreator('BLOCK 2.0',
                                                                                      'FTOW',
                                                                                      dates,
                                                                                      'LOSS',
                                                                                      0,
                                                                                      positiveOpenvalue[counter],
                                                                                      positiveOpenpos[counter],
                                                                                      positiveOpentime[counter],
                                                                                      positiveTPvalue[counter],
                                                                                      positiveTPpos[counter],
                                                                                      positiveTPtime[counter],
                                                                                      positiveSLvalue[counter],
                                                                                      positiveSLpos[counter],
                                                                                      possitiveSLltime[counter],
                                                                                      'price went to stop loss after trade open before reaching takeprofit')
                                    ftowTradeObjectList.append(ftowObject)
                                if SLafterTradeOpenPosition > positiveTPpos[counter]:
                                    # Price reaches take profit before stop loss
                                    profitloss.append('PROFIT')
                                    ftowObject = objectConstructors.ftowobjectcreator('BLOCK 3.0',
                                                                                      'FTOW',
                                                                                      dates,
                                                                                      'PROFIT',
                                                                                      3,
                                                                                      positiveOpenvalue[counter],
                                                                                      positiveOpenpos[counter],
                                                                                      positiveOpentime[counter],
                                                                                      positiveTPvalue[counter],
                                                                                      positiveTPpos[counter],
                                                                                      positiveTPtime[counter],
                                                                                      positiveSLvalue[counter],
                                                                                      positiveSLpos[counter],
                                                                                      possitiveSLltime[counter],
                                                                                      'Price reached take profit before hitting stop loss')
                                    ftowTradeObjectList.append(ftowObject)
                                if positiveSLpos[counter] == positiveTPpos[counter]:
                                    # There is a value for both. We  check for SIM
                                    profitloss.append('SIM')
                                    ftowObject = objectConstructors.ftowobjectcreator('BLOCK 4.0',
                                                                                      'FTOW',
                                                                                      dates,
                                                                                      'SIM',
                                                                                      0,
                                                                                      positiveOpenvalue[counter],
                                                                                      positiveOpenpos[counter],
                                                                                      positiveOpentime[counter],
                                                                                      positiveTPvalue[counter],
                                                                                      positiveTPpos[counter],
                                                                                      positiveTPtime[counter],
                                                                                      positiveSLvalue[counter],
                                                                                      positiveSLpos[counter],
                                                                                      possitiveSLltime[counter],
                                                                                      'Stoploss and takeprofit reachedith the same candle')
                    else:
                        # There are not TP values
                        if positiveSLpos[counter] != 'NONE':
                            # No Take profit values but there are values for SL
                            profitloss.append('LOSS')
                            ftowObject = objectConstructors.ftowobjectcreator('BLOCK 6.0',
                                                                              'FTOW',
                                                                              dates,
                                                                              'LOSS',
                                                                              0,
                                                                              positiveOpenvalue[counter],
                                                                              positiveOpenpos[counter],
                                                                              positiveOpentime[counter],
                                                                              positiveTPvalue[counter],
                                                                              positiveTPpos[counter],
                                                                              positiveTPtime[counter],
                                                                              positiveSLvalue[counter],
                                                                              positiveSLpos[counter],
                                                                              possitiveSLltime[counter],
                                                                              'There are no values for TP but there are for SL')
                            ftowTradeObjectList.append(ftowObject)
                        else:
                            # No value for SL and no value for TP
                            # Price never went through SL not TP. It just dicked around
                            profitloss.append('UNDETERMMINED')
                            ftowObject = objectConstructors.ftowobjectcreator('BLOCK 7.0',
                                                                              'FTOW',
                                                                              dates,
                                                                              'LOSS',
                                                                              0,
                                                                              positiveOpenvalue[counter],
                                                                              positiveOpenpos[counter],
                                                                              positiveOpentime[counter],
                                                                              positiveTPvalue[counter],
                                                                              positiveTPpos[counter],
                                                                              positiveTPtime[counter],
                                                                              positiveSLvalue[counter],
                                                                              positiveSLpos[counter],
                                                                              possitiveSLltime[counter],
                                                                              'Price never went through SL not TP. It just dicked around')
                            ftowTradeObjectList.append(ftowObject)
                if ftowid[counter] == 'Negative':
                    if negativeTPpos[counter] != 'NONE':
                        # Here we know there are values for Take Profit
                        if negativeSLpos[counter] == 'NONE':
                            # no values for stoploss
                            # 'There is a value for Take profit but no value for Stop loss'
                            # --BLOCK 1.0--
                            profitloss.append('PROFIT')
                            ftowObject = objectConstructors.ftowobjectcreator('BLOCK 8.0',
                                                                              'FTOW',
                                                                              dates,
                                                                              'PROFIT',
                                                                              3,
                                                                              negativeOpenvalue[counter],
                                                                              negativeOpenpos[counter],
                                                                              negativeOpentime[counter],
                                                                              negativeTPvalue[counter],
                                                                              negativeTPpos[counter],
                                                                              negativeTPtime[counter],
                                                                              negativeSLvalue[counter],
                                                                              negativeSLpos[counter],
                                                                              negativeSLltime[counter],
                                                                              'There is a value for Take profit but no value for Stop loss')
                            ftowTradeObjectList.append(ftowObject)
                        else:
                            # here we have values for both sl and tp
                            # first check for the SL values after trade open
                            stoplossvalues = extractors.stringpositionextractor(negativeSLstring[counter])
                            for items in stoplossvalues:
                                if items > negativeOpenpos:
                                    checkList.append(items)
                                    checkBool = True
                            if checkBool:
                                # Here we know that there are possibility for SL
                                # We now check all the possible itteration
                                # SL > TP. TP > SL. TP == SL
                                SLafterTradeOpenPosition = checkList[0]
                                # Here we now that there are values for SL after trade open
                                if SLafterTradeOpenPosition < negativeTPpos[counter]:
                                    # price went to stop loss after trade open before reaching takeprofit
                                    profitloss.append('LOSS')
                                    ftowObject = objectConstructors.ftowobjectcreator('BLOCK 9.0',
                                                                                      'FTOW',
                                                                                      dates,
                                                                                      'LOSS',
                                                                                      0,
                                                                                      negativeOpenvalue[counter],
                                                                                      negativeOpenpos[counter],
                                                                                      negativeOpentime[counter],
                                                                                      negativeTPvalue[counter],
                                                                                      negativeTPpos[counter],
                                                                                      negativeTPtime[counter],
                                                                                      negativeSLvalue[counter],
                                                                                      negativeSLpos[counter],
                                                                                      negativeSLltime[counter],
                                                                                      'price went to stop loss after trade open before reaching takeprofit')
                                    ftowTradeObjectList.append(ftowObject)
                                if SLafterTradeOpenPosition > negativeTPpos[counter]:
                                    # Price reaches take profit before stop loss
                                    profitloss.append('PROFIT')
                                    ftowObject = objectConstructors.ftowobjectcreator('BLOCK 10.0',
                                                                                      'FTOW',
                                                                                      dates,
                                                                                      'PROFIT',
                                                                                      3,
                                                                                      negativeOpenvalue[counter],
                                                                                      negativeOpenpos[counter],
                                                                                      negativeOpentime[counter],
                                                                                      negativeTPvalue[counter],
                                                                                      negativeTPpos[counter],
                                                                                      negativeTPtime[counter],
                                                                                      negativeSLvalue[counter],
                                                                                      negativeSLpos[counter],
                                                                                      possitiveSLltime[counter],
                                                                                      'Price reached take profit before hitting stop loss')
                                    ftowTradeObjectList.append(ftowObject)
                                if negativeSLpos[counter] == negativeTPpos[counter]:
                                    # There is a value for both. We  check for SIM
                                    profitloss.append('SIM')
                                    ftowObject = objectConstructors.ftowobjectcreator('BLOCK 11.0',
                                                                                      'FTOW',
                                                                                      dates,
                                                                                      'SIM',
                                                                                      0,
                                                                                      negativeOpenvalue[counter],
                                                                                      negativeOpenpos[counter],
                                                                                      negativeOpentime[counter],
                                                                                      negativeTPvalue[counter],
                                                                                      negativeTPpos[counter],
                                                                                      negativeTPtime[counter],
                                                                                      negativeSLvalue[counter],
                                                                                      negativeSLpos[counter],
                                                                                      negativeSLltime[counter],
                                                                                      'Stoploss and takeprofit reachedith the same candle')
                    else:
                        # There are not TP values
                        if negativeSLpos[counter] != 'NONE':
                            # No Take profit values but there are values for SL
                            profitloss.append('LOSS')
                            ftowObject = objectConstructors.ftowobjectcreator('BLOCK 12.0',
                                                                              'FTOW',
                                                                              dates,
                                                                              'LOSS',
                                                                              0,
                                                                              negativeOpenvalue[counter],
                                                                              negativeOpenpos[counter],
                                                                              negativeOpentime[counter],
                                                                              negativeTPvalue[counter],
                                                                              negativeTPpos[counter],
                                                                              negativeTPtime[counter],
                                                                              negativeSLvalue[counter],
                                                                              negativeSLpos[counter],
                                                                              possitiveSLltime[counter],
                                                                              'There are no values for TP but there are for SL')
                            ftowTradeObjectList.append(ftowObject)
                        else:
                            # No value for SL and no value for TP
                            # Price never went through SL not TP. It just dicked around
                            profitloss.append('UNDETERMMINED')
                            ftowObject = objectConstructors.ftowobjectcreator('BLOCK 13.0',
                                                                              'FTOW',
                                                                              dates,
                                                                              'LOSS',
                                                                              0,
                                                                              negativeOpenvalue[counter],
                                                                              negativeOpenpos[counter],
                                                                              negativeOpentime[counter],
                                                                              negativeTPvalue[counter],
                                                                              negativeTPpos[counter],
                                                                              negativeTPtime[counter],
                                                                              negativeSLvalue[counter],
                                                                              negativeSLpos[counter],
                                                                              possitiveSLltime[counter],
                                                                              'Price never went through SL not TP. It just dicked around')
                            ftowTradeObjectList.append(ftowObject)
            else:
                profitloss.append('NONE')
                ftowTradeObjectList.append('NONE')
        else:
            profitloss.append('NONE')
            ftowTradeObjectList.append('NONE')
        counter = counter + 1
        checkList.clear()
        checkBool = False
    return profitloss,ftowTradeObjectList




