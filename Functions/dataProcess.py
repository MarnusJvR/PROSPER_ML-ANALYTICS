import pandas
from globalVariables import pipValues
from Helpers import extractors
from Helpers import Calculators
from Helpers import gapIdentifyer
from priceTrackers import gapClosing
from priceTrackers import stoplossPositions
from priceTrackers import fiftyPercentGapPositions
from priceTrackers import fiftyPercentGapReversePositions
from priceTrackers import priceMoveThroughGapOpenPositions
from priceTrackers import gapFiftyTakeProfitPositions
from priceTrackers import gapcTakeProfitPositions
from Functions import gapcProfitLoss
from Functions import gapfiftyProfitLoss


# -----LIST OF VARIABLES-----:
#
# ----GENERAL-----
#
# actualDateList: Contains df1 date objects
# closingValues: originally contains close values df1. I change this list to become the prev closing values line 50
# closingList: DF2 - (Mondays & Fridays) closing values
# difList: contains all df1 gapsizes
# dateListdf2: DF2 list of date objects
# dateList: Contains df1 list of raw dateTimes. Unprocessed.
# gapsizesetnumber: pipvalue of positive gapsize
# gapClass: DF2 with gap class identefyer (weekend)
# gapCloseNum: number of candles from gap opening that gap was closed
# gapCloseStr: String of all variables where price went through close
# gapSizeList: DF2 list of gap sizes
# negativegapsizesetnumber : pipvalue of negative gapsize
# prevClosingValue: DF2 values of prev closing
# priceMoveOpenPosition: positions where price go back through open after going to 50%
# priceMoveOpenPosition: list of position strings where price went back through open
# reverseHalveHitPosstr: list of halve hit reverse positions
# reverseHalveHit: Contains 'HIT' valies for all gaps that go through 50% in revers (after closing the gap offcourse)
# reversehalvehitposstr: contains all the positions for reverse going through 50%
# reverseHalveHitTimestr: all times that price go through 50% in reverse after gap was closed
# timeTrackerStr: All the time values price went through close
# weekdayList: df1 list of weekdays # Monday= 0 Tuesday = 1 Wednesday = 2 Thursday = 3 Friday = 4
# rangeHigh: itterations that price movements are checked (MAX). Smaller candles = higher rangehigh




#
# ----GAPFIFTY VARIABLES------
#
# gapFiftyOpenTime: open time for GAPFIFTY (when price go back through gap open value)
# gapFiftyOpenTimeStr: string of times where price went back through open value after going to fifty
# gapfiftyOpenPos: position that gap fifty strategy opened
# gapfiftyStoplossValueList: Stoploss values for GAPFIFTTY
# gapfiftyOpenPos: open position for GAPFIFTY
# gapfiftytpPos: Position where price went through tp
# gapfiftyTpTimeStr: list of time strings of where price went past tp
# gapfiftytptime: Time price went through tp
# gapfiftytpvalue: value of take profit
# gapFiftyOpenTime: Time that gapfifty opened
# gapFiftyOpenTimeStr: times that price was beyond open
# gapfiftytpstr: string of positions where price went through tp
# gapfiftyStoplossValueList: Stoploss value for GAPFIFTY
# gapfiftyStoplossValueList: Stoploss value for GAPFIFTY
# High: DF2 list of high candle values
# openValueListDf2: openvalues DF2
# Low: DF2 list of low candle values
# myTime: DF2 list of time strings
# myDate: DF2 list of date objects
# stoploss : pipvalue of stoploss ( egg 0.0015)
# totalGaps: total amount of gaps that opened
# tradeList: shows where price closed the gap
# timeStrings: list of time df1 in str



# ---GAPCVARIABLES----
# gapcOpenPos: Open position for GAPC strategy
# gapcOpenTimeFalse: this gives us the first time price reversed back through 50%. To be a gapc it must first pass the check to go to gap close
# gapcStoplossPositions: Stoploss positions: Gapc
# gapcStoplossTimeStrings: Timestrings for stoploss Gapc
# gapcStoplossValueList: Stoploss values for gapc
# gapcTakeProfitValue: contains the take profit values for GAPC
# gapcStoplossValueList: Stoploss values for GAPC strategy



# -----PROCESS-----
# 1- Pairname recieved.
# 2- Global variables are calculated and called
# 3- Filename extracted
# 4- Readfile and create Data Frame Df1
# 5- Extract date object and time seperatly from dateTime string
# 6- Extract weekdays from date objects
# 7- insert a new list into df1 containing the previous closing values. This is needed to identify price gaps (prev close - open)
# 8- Calculate gapsizes
# 9- Extract only Monday and Friday
# 10- Check for weekend gaps
# 11- Check what gaps closed
# 12- Determine halve gape values (50%)
# 13- Calculate stoploss values for GAPC strategy
# 14- Calculate stoploss for GAPFIFTY strategy
# 15. We now check for price movement through 50% gap. 2 FUNCTIONS: BOTH DIRECTIONS
# 16. We now check for price movement through 50% gap in the reverse direction
# 17. Track all the instances where price go through open value after going to 50% for gapfifty
# 18. Check if price price reached Take Profit for GAPFIFTY
# 19. Determine when GAPFIFTY strategy opened (GAPFIFTY IFENTIFYER)
# 20. Determine GAPC take profit values


def readDataframe(pair):
    #
    # 2- Global variables are calculated and called
    #
    stoploss, negativegapsizesetnumber, gapsizesetnumber, rangeHigh = pipValues.setPipValues(pair)
    #
    # 3- Filename extracted
    #
    fileName = 'CSV/' + pair + '.csv'
    df1 = pandas.read_csv(fileName, header=None)
    df1.columns = ["DateTime", "Opening Value", "High", "low", "Close Value"]
    dateList = list(df1.loc[:, 'DateTime'])
    #
    # 5- Extract date object and time seperatly from dateTime string
    #
    print('--------------------------------')
    print('calling date extractor')
    timeStrings, actualDateList = extractors.dateStringExtractor(dateList)
    df1 = df1.drop("DateTime", 1)
    df1["Time"] = timeStrings
    df1["DATE_OBJECT"] = actualDateList
    #
    # 6- Extract weekdays from date objects---
    #
    print('--------------------------------')
    print('calling weekday extractor')
    weekdayList = extractors.weekdayExtractor(actualDateList)
    df1['Weekday'] = weekdayList
    #
    # 7- insert a new list into df1 containing the previous closing values. This is needed to identify price gaps (prev close - open)
    #
    closingValues = list(df1.loc[:, 'Close Value'])
    openValueList = list(df1.loc[:, 'Opening Value'])
    closingvalueinsertfirstitteration = openValueList[0]
    closingValues.insert(0, closingvalueinsertfirstitteration)
    closingValues.pop()
    df1['PREV_CLOSING_VAL'] = closingValues
    # -----------------------------------------------ANALYTICS FILE----------------------------------------------
    df1.to_csv('analytics/fullset.csv')
    # -----------------------------------------------ANALYTICS FILE----------------------------------------------
    #
    # 8- Calculate gapsizes
    #
    # Remember that we have just changed the content from close value list to prev close values
    print('--------------------------------')
    print('calling calculator')
    difList = Calculators.gapsizecalc(openValueList, closingValues)
    df1['GAP_SIZE'] = difList
    # here I need to progresively elemenate weekdays.
    # there might be a more effective way to do this
    # Monday= 0 Tuesday = 1 Wednesday = 2 Thursday = 3 Friday = 4
    # We want closing on 4 ! opening on 1 !
    df2 = df1[df1.Weekday != 1]
    df2 = df2[df2.Weekday != 2]
    df2 = df2[df2.Weekday != 3]
    df2 = df2[df2.Weekday != 5]
    df2 = df2[df2.Weekday != 6]
    closingList = list(df2.loc[:, 'Close Value'])
    #
    # 10- Check for weekend gaps
    #
    # -----------------------------------------------ANALYTICS FILE----------------------------------------------
    df2.to_csv('analytics/DF2.csv')
    # -----------------------------------------------ANALYTICS FILE----------------------------------------------
    gapSizeList = list(df2.loc[:, 'GAP_SIZE'])
    myTime = list(df2.loc[:, 'Time'])
    myDate = list(df2.loc[:, 'DATE_OBJECT'])
    dateListdf2 = list(df2.loc[:, 'DATE_OBJECT'])
    gapClass = gapIdentifyer.gapIdentifyer(pair, gapSizeList, myDate, gapsizesetnumber, negativegapsizesetnumber)

    totalGaps = Calculators.gapCalculator(gapClass)
    #
    # 11- Check what gaps closed
    #
    High = list(df2.loc[:, 'High'])
    Low = list(df2.loc[:, 'low'])
    # these are my itteration stoppers not to look beyond list end
    stopNumber, stopHighNumber = pipValues.stopLists(Low, High)
    prevClosingValue = list(df2.loc[:, 'PREV_CLOSING_VAL'])
    print('--------------------------------')
    print('calling gapClosePositionCalc')

    tradeList, gapCloseNum, gapCloseStr, timeTrackerStr, gapCloseTime = gapClosing.gapClosePositionCalc(gapSizeList,
                                                                                                        gapClass,
                                                                                                        rangeHigh,
                                                                                                        stopNumber,
                                                                                                        stopHighNumber,
                                                                                                        Low, High,
                                                                                                        prevClosingValue,
                                                                                                        myTime)
    df2['GAP_CLOSED'] = tradeList
    df2['GAP_CLOSED_AT'] = gapCloseNum
    openValueListDf2 = list(df2.loc[:, 'Opening Value'])
    #
    # 12- Calculate halve gap values
    #
    print('--------------------------------')
    print('Halvegap value calculator called')
    halveGapValue = Calculators.fiftypercentgapvalue(gapClass, openValueListDf2, prevClosingValue)
    df2['50%_GAP_VALUE'] = halveGapValue
    print('--------------------------------')
    print('Calling stoploss value calculater GAPC')
    #
    # # 13- Calculate stoploss values for GAPC strategy
    #
    gapcStoplossValueList = Calculators.stopLossValues(halveGapValue, stoploss, gapClass, gapSizeList)
    #
    # 14- Calculate stoploss for GAPFIFTY strategy
    #
    print('--------------------------------')
    print('Calling stoploss value calculater GAPFIFTY')
    gapfiftyStoplossValueList = Calculators.stopLossValues(openValueListDf2, stoploss, gapClass, gapSizeList)
    #
    # 14- Find all positions where price go through Stoploss: GAPC
    #
    print('--------------------------------')
    print('Calling stoploss position calculater GAPC')
    gapcStoplossPositions, gapcStoplossTimeStrings = stoplossPositions.checkStopLossPositions(gapClass, gapSizeList,
                                                                                              rangeHigh, stopNumber,
                                                                                              Low, High,
                                                                                              gapcStoplossValueList,
                                                                                              myTime)
    #
    # 14- Find all positions where price go through Stoploss: GAPFIFTY
    #
    print('--------------------------------')
    print('Calling stoploss position calculater GAPFIFTY')
    gapFiftyStoplossPositions, gapFiftyStoplossTimeStrings = stoplossPositions.checkStopLossPositions(gapClass,
                                                                                                      gapSizeList,
                                                                                                      rangeHigh,
                                                                                                      stopNumber, Low,
                                                                                                      High,
                                                                                                      gapfiftyStoplossValueList,
                                                                                                      myTime)

    #
    # 15. We now check for price movement through 50% gap. 2 FUNCTIONS: BOTH DIRECTIONS
    #
    print('--------------------------------')
    print('Calling 50% gap position calculater GAPFIFTY')
    halveHitPositionStr, halveHitTimeStr, halveHit, halveHitPosition = fiftyPercentGapPositions.fiftypercentpositions(
        gapClass, gapSizeList, halveGapValue, rangeHigh, stopNumber, Low, High, myTime)
    #
    # 16. We now check for price movement through 50% gap in the reverse direction
    #
    print('--------------------------------')
    print('Calling reverse 50% gap position calculater GAPFIFTY')
    reverseHalveHit, reverseHalveHitPosstr, gapcOpenPos, gapcOpenTimeFalse, reverseHalveHitTimestr = fiftyPercentGapReversePositions.fiftypercentpositionreverse(
        gapClass, gapSizeList, halveGapValue, gapCloseNum, rangeHigh, stopNumber, Low, High, myTime)

    #
    # 17. Track all the instances where price go through open value after going to 50% for gapfifty
    #
    print('--------------------------------')
    print('Calling the price move through open calculator')
    gapfiftyOpenPos, priceMoveOpenPosition, gapFiftyOpenTime, gapFiftyOpenTimeStr = priceMoveThroughGapOpenPositions.priceTrackGapOpening(
        gapClass, gapSizeList, openValueListDf2, halveHit, rangeHigh, stopNumber, Low, High, myTime)
    #
    # 18. Check if price price reached Take Profit for GAPFIFTY
    #
    print('--------------------------------')
    print('Calling the GAPFIFTY take profit calculator')
    gapfiftytpPos, gapfiftytpstr, gapfiftytpvalue, gapfiftytptime, gapfiftyTpTimeStr = gapFiftyTakeProfitPositions.gapfiftytpcalculator(
        gapClass, gapSizeList, openValueListDf2, rangeHigh, stopNumber, Low, High, myTime)
    #
    # 19. Determine when GAPFIFTY strategy opened (GAPFIFTY IFENTIFYER)
    #
    gapFiftyID = Calculators.gapfiftyidentifyer(gapfiftyOpenPos, gapCloseNum)
    #
    # 20. Determine GAPC take profit values
    #
    gapcTakeProfitValue = Calculators.gapctpvaluecalc(gapClass, gapSizeList, openValueListDf2)
    #
    # 21. GAPC take profit positions
    #
    gapcTpPos, gapcTpPosStr, gapcTpTime, gapcTpTimeStr = gapcTakeProfitPositions.gapctakeprofitposcalculator(gapClass,
                                                                                                             gapSizeList,
                                                                                                             gapcTakeProfitValue,
                                                                                                             rangeHigh,
                                                                                                             stopNumber,
                                                                                                             Low, High,
                                                                                                             myTime)
    #
    # 22. Calculate Profit for GAPC
    #
    gapcProfitLossList, gapcObjectList = gapcProfitLoss.gapcprofitlosscalc(gapcOpenPos,
                                                                           halveGapValue,
                                                                           gapcStoplossValueList,
                                                                           gapcTpPos,
                                                                           gapcTakeProfitValue,
                                                                           gapcStoplossPositions,
                                                                           gapcTpPosStr,
                                                                           dateListdf2,
                                                                           gapCloseNum,
                                                                           gapCloseStr,
                                                                           gapCloseTime,
                                                                           gapcOpenTimeFalse,
                                                                           gapcTpTime,
                                                                           gapcStoplossTimeStrings)
    print('----------------------------GAPC TESTING------------------------------------------------')
    for items in gapcObjectList:
        if items != 'NONE':
            print('--------------------')
            print(items.date)
            print(items.name)
            print(items.profitloss)
            print('rvalue')
            print(items.rvalue)
            print('gapclosepos')
            print(items.gapclosepos)
            print('gapcopenpos')
            print(items.gapcopenpos)
            print('tpvalue')
            print(items.tpvalue)
            print('slvalue')
            print(items.slvalue)
            print('tppos')
            print(items.tppos)
            print('slpos')
            print(items.slpos)
            print('gapclosetime')
            print(items.gapclosetime)
            print('gapcopentime')
            print(items.gapcopentime)
            print('takeprofittime')
            print(items.takeprofittime)
            print(items.stoplossstime)
            print('--------------------')
    print('----------------------------END------------------------------------------------')
    #
    # 23.Calculate profitloss for gapfifty
    #
    gapfiftyObjectList, gapFiftyprofitLossList = gapfiftyProfitLoss.gapfiftyprofitlosscalculator(gapfiftyOpenPos,
                                                                                                 gapFiftyID,
                                                                                                 openValueListDf2,
                                                                                                 gapfiftyStoplossValueList,
                                                                                                 gapfiftytpvalue,
                                                                                                 gapFiftyStoplossPositions,
                                                                                                 gapfiftytpstr,
                                                                                                 dateListdf2,
                                                                                                 halveGapValue,
                                                                                                 halveHitPosition,
                                                                                                 gapfiftytptime,
                                                                                                 gapFiftyOpenTime,
                                                                                                 halveHitTimeStr,
                                                                                                 gapFiftyStoplossTimeStrings)
    print(len(str(gapcProfitLossList)))
    print(len(str(gapcObjectList)))
    print(len(str(gapFiftyprofitLossList)))
    print(len(str(gapfiftyObjectList)))
    print('----------------------------GAPC FIFTY------------------------------------------------')
    for items in gapfiftyObjectList:
        if items != 'NONE':
            print('--------------------')
            print(items.date)
            print(items.name)
            print(items.profitloss)
            print('rvalue')
            print(items.rvalue)
            print('fiftypercentvalue')
            print(items.fiftypercentvalue)
            print('fiftypercentpos')
            print(items.fiftypercentpos)
            print('gapopenvalue')
            print(items.gapopenvalue)
            print('tradeopenpos')
            print(items.tradeopenpos)
            print('slvalue')
            print(items.slvalue)
            print('tpvalue')
            print(items.tpvalue)
            print('tppos')
            print(items.tppos)
            print('gapfiftytptime')
            print(items.gapfiftytptime)
            print('takeprofittime')
            print(items.gapFiftyOpenTime)
            print('halvehittime')
            print(items.halvehittime)
            print('stoplosstimstr')
            print('comment')
            print(items.comment)
            print('--------------------')
    print('----------------------------END------------------------------------------------')


    df2["GAP_CLASS"] = gapClass
    df2['Reverse_Halve_Hit'] = reverseHalveHit
    df2['reverseHalveHitPosstr'] = reverseHalveHitPosstr
    df2['GAPC_OPEN_POSITION'] = gapcOpenPos
    df2['GAPC_OPEN_TIME'] = gapcOpenTimeFalse
    df2['Reverse_HalveHitTimeStr'] = reverseHalveHitTimestr
    df2['gapFiftyID'] = gapFiftyID
    df2['gapfiftytpPos'] = gapfiftytpPos
    df2['gapfiftytpstr'] = gapfiftytpstr
    df2['gapfiftytpvalue'] = gapfiftytpvalue
    df2['gapfiftytptime'] = gapfiftytptime
    df2['gapfiftyTpTimeStr'] = gapfiftyTpTimeStr
    df2['gapfiftyOpenPos'] = gapfiftyOpenPos
    df2['priceMoveOpenPosition'] = priceMoveOpenPosition
    df2['gapFiftyOpenTime'] = gapFiftyOpenTime
    df2['gapFiftyOpenTimeStr'] = gapFiftyOpenTimeStr
    df2['GAP50_SL_POSITIONS'] = gapFiftyStoplossPositions
    df2['GAP50_SL_TIMES'] = gapFiftyStoplossTimeStrings
    df2['GAPC_SL_POSITIONS'] = gapcStoplossPositions
    df2['GAPC_SL_TIMES'] = gapcStoplossTimeStrings

    return actualDateList
