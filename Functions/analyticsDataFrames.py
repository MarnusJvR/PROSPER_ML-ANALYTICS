import pandas
from tkinter import *
import sys

def gapcDataFrameCreator(pair,tradeobjectlist):
    # Creating the data frames for analysis
    pairList = []
    block = []
    name= []
    date= []
    profitLoss= []
    rvalue= []
    gapclosepos= []
    gapcopenpos= []
    tpvalue= []
    slvalue= []
    tppos= []
    slpos= []
    gapclosetime= []
    gapcopentime= []
    takeprofittime= []
    stoplossstime= []
    comment= []
    gapsize = []
    profit = 0
    loss = 0
    total = 0
    sim = 0
    un = 0
    profit1 = 0
    loss1 = 0
    total1 = 0
    sim1 = 0
    un1 = 0
    profit2 = 0
    loss2 = 0
    total2 = 0
    sim2 = 0
    un2 = 0
    profit3 = 0
    loss3 = 0
    total3 = 0
    sim3 = 0
    un3 = 0
    profit4 = 0
    loss4 = 0
    total4 = 0
    sim4 = 0
    un4 = 0
    profit5 = 0
    loss5 = 0
    total5 = 0
    sim5 = 0
    un5 = 0
    profit6 = 0
    loss6 = 0
    total6 = 0
    sim6 = 0
    un6 = 0
    profit7 = 0
    loss7 = 0
    total7 = 0
    sim7 = 0
    un7 = 0
    rvalueCalc = 0
    rvalueCalc1 = 0
    rvalueCalc2 = 0
    rvalueCalc3 = 0
    rvalueCalc4 = 0
    rvalueCalc5 = 0
    rvalueCalc6 = 0
    rvalueCalc7 = 0
    for objects in tradeobjectlist:
        if objects != 'NONE':
            pairList.append(pair)
            block.append(objects.block)
            name.append(objects.name)
            date.append(objects.date)
            profitLoss.append(objects.profitLoss)
            rvalue.append(objects.rvalue)
            gapclosepos.append(objects.gapclosepos)
            gapcopenpos.append(objects.gapcopenpos)
            tpvalue.append(objects.tpvalue)
            slvalue.append(objects.slvalue)
            tppos.append(objects.tppos)
            slpos.append(objects.slpos)
            gapclosetime.append(objects.gapclosetime)
            gapcopentime.append(objects.gapcopentime)
            takeprofittime.append(objects.takeprofittime)
            stoplossstime.append(objects.stoplossstime)
            comment.append(objects.comment)
            gapsize.append(objects.gapsize)
            print('-------GAPC---------')
            print(objects.profitLoss)
            print(objects.block)
            print('----------------')
            if objects.profitLoss == 'Profit':
                print('if objects.profitLoss == Profit:')
                profit = profit + 1
                rvalueCalc = rvalueCalc + objects.rvalue
            if objects.profitLoss == 'Loss':
                print('if objects.profitLoss == Loss:')
                loss = loss + 1
                rvalueCalc = rvalueCalc + objects.rvalue
            if objects.profitLoss == 'SIM':
                print('if objects.profitLoss == SIM:')
                sim = sim + 1
            if objects.profitLoss == 'Undetermined':
                print('if objects.profitLoss == un:')
                un = un + 1
            total = total + 1
            # block 1
            if objects.block == 'Block 1.0':
                total1 = total1 + 1
            if objects.block == 'Block 1.0' and objects.profitLoss == 'Profit':
                print('BLOCK 1 if objects.profitLoss == Profit:')
                profit1 = profit1 + 1
                rvalueCalc1 = rvalueCalc1 + objects.rvalue
            # BLOCK 2
            if objects.block == 'Block 2.0':
                total2 = total2 + 1
                loss2 = loss2 + 1
                rvalueCalc2 = rvalueCalc2 + objects.rvalue
            # BLOCK 3
            if objects.block == 'Block 3.0':
                total3 = total3 + 1
                sim3 = sim3 + 1
            # BLOCK 4
            if objects.block == 'Block 4.0':
                total3 = total3 + 1
                loss4 = loss4 + 1
                rvalueCalc4 = rvalueCalc4 + objects.rvalue
            # BLOCK 5
            if objects.block == 'Block 5.0':
                total5 = total5 + 1
                loss5 = loss5 + 1
                rvalueCalc5 = rvalueCalc5 + objects.rvalue
            # BLOCK 6
            if objects.block == 'Block 6.0':
                total6 = total6 + 1
                profit6 = profit6 + 1
                rvalueCalc6 = rvalueCalc6 + objects.rvalue
            # BLOCK 7
            if objects.block == 'Block 7.0':
                total7 = total7 + 1
                un7 = un7 + 1
    # Now I have totals/ It is time to create data frames
    #  First is the data frame carrying all the trades
    dfGapcTradeObjects = pandas.DataFrame()
    dfGapcTradeObjects['Pair'] = pairList
    dfGapcTradeObjects['block'] = block
    dfGapcTradeObjects['date'] = date
    dfGapcTradeObjects['profitLoss'] = profitLoss
    dfGapcTradeObjects['rvalue'] = rvalue
    dfGapcTradeObjects['gapclosepos'] = gapclosepos
    dfGapcTradeObjects['gapcopenpos'] = gapcopenpos
    dfGapcTradeObjects['tpvalue'] = tpvalue
    dfGapcTradeObjects['slvalue'] = slvalue
    dfGapcTradeObjects['tppos'] = tppos
    dfGapcTradeObjects['slpos'] = slpos
    dfGapcTradeObjects['gapclosetime'] = gapclosetime
    dfGapcTradeObjects['gapcopentime'] = gapcopentime
    dfGapcTradeObjects['takeprofittime'] = takeprofittime
    dfGapcTradeObjects['stoplossstime'] = stoplossstime
    dfGapcTradeObjects['comment'] = comment
    dfGapcTradeObjects['Gap Size'] = gapsize
    # Second is the breakdown of block totals
    # Create tupple objects
    def calcrate(profitnum, totalnum):
        if totalnum != 0:
            winrateret = profitnum/totalnum*100
        else:
            winrateret = 0
        return winrateret

    winrateTotal = profit / total * 100
    totalTuple = (
    'Total', 'Block 1.0', 'Block 2.0', 'Block 3.0', 'Block 4.0', 'Block 5.0', 'Block 6.0', 'Block 7.0', 'Block 8.0')
    winrateTotal1 = calcrate(profit1, total1)
    winrateTotal2 = calcrate(profit2, total2)
    winrateTotal3 = calcrate(profit3, total3)
    winrateTotal4 = calcrate(profit4, total4)
    winrateTotal5 = calcrate(profit5, total5)
    winrateTotal6 = calcrate(profit6, total6)
    winrateTotal7 = calcrate(profit7, total7)

    totalTuple1 = (total, total1, total2, total3, total4, total5, total6, total7)
    totalTuple2 = (profit, profit1, profit2, profit3, profit4, profit5, profit6, profit7)
    totalTuple3 = (loss, loss1, loss2, loss3, loss4, loss5, loss6, loss7)
    totalTuple4 = (sim, sim1, sim2, sim3, sim4, sim5, sim6, sim7)
    totalTuple5 = (un, un1, un2, un3, un4, un5, un6, un7)
    totalTuple6 = (
    rvalueCalc, rvalueCalc1, rvalueCalc2, rvalueCalc3, rvalueCalc4, rvalueCalc5, rvalueCalc6, rvalueCalc7)
    totalTuple7 = (
    winrateTotal, winrateTotal1, winrateTotal2, winrateTotal3, winrateTotal4, winrateTotal5, winrateTotal6,
    winrateTotal7, winrateTotal7)




    # winrateTotal = profit/total*100
    # totalTuple = ('Total',total,profit,loss,sim,un,rvalueCalc,winrateTotal)
    # if total1 != 0:
    #     winrateTotal1 = profit1 / total1 * 100
    # else:
    #     winrateTotal1 = 0
    # totalTuple1 = ('Block 1.0', total1, profit1, loss1, sim1, un1, rvalueCalc1, winrateTotal1)
    # if total2 != 0:
    #     winrateTotal2 = profit2 / total2 * 100
    # else:
    #     winrateTotal2 = 0
    # totalTuple2 = ('Block 2.0', total2, profit2, loss2, sim2, un2, rvalueCalc2, winrateTotal2)
    # if total3 != 0:
    #     winrateTotal3 = profit3 / total3 * 100
    # else:
    #     winrateTotal3 = 0
    # totalTuple3 = ('Block 3.0', total3, profit3, loss3, sim3, un3, rvalueCalc3, winrateTotal3)
    # if total4 != 0:
    #     winrateTotal4 = profit4 / total4 * 100
    # else:
    #     winrateTotal4 = 0
    # totalTuple4 = ('Block 4.0', total4, profit4, loss4, sim4, un4, rvalueCalc4, winrateTotal4)
    # if total5 != 0:
    #     winrateTotal5 = profit5 / total5 * 100
    # else:
    #     winrateTotal5 = 0
    # totalTuple5 = ('Block 5.0', total5, profit5, loss5, sim5, un5, rvalueCalc5, winrateTotal5)
    # if total6 != 0:
    #     winrateTotal6 = profit6 / total6 * 100
    # else:
    #     winrateTotal6 = 0
    # totalTuple6 = ('Block 6.0', total6, profit6, loss6, sim6, un6, rvalueCalc6, winrateTotal6)
    # if total7 != 0:
    #     winrateTotal7 = profit7 / total7 * 100
    # else:
    #     winrateTotal7 = 0
    # totalTuple7 = ('Block 7.0', total7, profit7, loss7, sim7, un7, rvalueCalc7, winrateTotal7)
    data_tuples = list(zip(totalTuple, totalTuple1,totalTuple2,totalTuple3,totalTuple4,totalTuple5,totalTuple6,totalTuple7))
    totalsDf = pandas.DataFrame(data_tuples, columns=['Name','Total','Profit','Loss','Sim','Un','R-value','Win Rate %'])
    return(totalsDf,dfGapcTradeObjects)


def gapFiftyAnal(pair,tradeobjectlist):
    # Creating the data frames for analys
    pairList = []
    block = []
    name= []
    date= []
    profitLoss= []
    rvalue= []
    fiftypercentvalue = []
    fiftypercentpos = []
    gapopenvalue = []
    tradeopenpos = []
    slvalue = []
    tpvalue = []
    slpos = []
    tppos = []
    gapfiftytptime = []
    gapFiftyOpenTime = []
    halvehittime = []
    stoplosstimstr = []
    comment = []
    gapsize = []
    profit = 0
    loss = 0
    total = 0
    sim = 0
    un = 0
    profit1 = 0
    loss1 = 0
    total1 = 0
    sim1 = 0
    un1 = 0
    profit2 = 0
    loss2 = 0
    total2 = 0
    sim2 = 0
    un2 = 0
    profit3 = 0
    loss3 = 0
    total3 = 0
    sim3 = 0
    un3 = 0
    profit4 = 0
    loss4 = 0
    total4 = 0
    sim4 = 0
    un4 = 0
    profit5 = 0
    loss5 = 0
    total5 = 0
    sim5 = 0
    un5 = 0
    profit6 = 0
    loss6 = 0
    total6 = 0
    sim6 = 0
    un6 = 0
    profit7 = 0
    loss7 = 0
    total7 = 0
    sim7 = 0
    un7 = 0
    profit8 = 0
    loss8 = 0
    total8 = 0
    sim8 = 0
    un8 = 0
    rvalueCalc = 0
    rvalueCalc1 = 0
    rvalueCalc2 = 0
    rvalueCalc3 = 0
    rvalueCalc4 = 0
    rvalueCalc5 = 0
    rvalueCalc6 = 0
    rvalueCalc7 = 0
    rvalueCalc8 = 0
    for objects in tradeobjectlist:
        if objects != 'NONE':
            pairList.append(pair)
            block.append(objects.block)
            name.append(objects.name)
            date.append(objects.date)
            profitLoss.append(objects.profitLoss)
            rvalue.append(objects.rvalue)
            fiftypercentvalue.append(objects.fiftypercentvalue)
            fiftypercentpos.append(objects.fiftypercentpos)
            gapopenvalue.append(objects.gapopenvalue)
            tradeopenpos.append(objects.tradeopenpos)
            tpvalue.append(objects.tpvalue)
            slvalue.append(objects.slvalue)
            tppos.append(objects.tppos)
            slpos.append(objects.slpos)
            gapfiftytptime.append(objects.gapfiftytptime)
            gapFiftyOpenTime.append(objects.gapFiftyOpenTime)
            comment.append(objects.comment)
            halvehittime.append(objects.halvehittime)
            stoplosstimstr.append(objects.stoplosstimstr)
            gapsize.append(objects.gapsize)
            print('-------GAPFIFTY---------')
            print(objects.profitLoss)
            print(objects.block)
            print('----------------')
            if objects.profitLoss == 'profit':
                print('if objects.profitLoss == Profit:')
                print(objects.rvalue)
                profit = profit + 1
                rvalueCalc = rvalueCalc + objects.rvalue
            if objects.profitLoss == 'LOSS':
                print('if objects.profitLoss == LOSS:')
                loss = loss + 1
                print(objects.rvalue)
                rvalueCalc = rvalueCalc + objects.rvalue
            if objects.profitLoss == 'SIM':
                print('if objects.profitLoss == SIM:')
                sim = sim + 1
            if objects.profitLoss == 'UNDETERMINED':
                print('if objects.profitLoss == un:')
                un = un + 1
            total = total + 1
            # BLOCK 1
            if objects.block == 'Block 1.0':
                total1 = total1 + 1
                loss1 = loss1 + 1
                rvalueCalc1 = rvalueCalc1 + objects.rvalue
            # BLOCK 2
            if objects.block == 'Block 2.0':
                total2 = total2 + 1
                loss2 = loss2 + 1
                rvalueCalc2 = rvalueCalc2 + objects.rvalue
            # BLOCK 3
            if objects.block == 'Block 3.0':
                total3 = total3 + 1
                profit3 = profit3 + 1
                rvalueCalc3 = rvalueCalc3 + objects.rvalue
            # BLOCK 4
            if objects.block == 'Block 4.0':
                total3 = total3 + 1
                sim4 = sim4 + 1
            # BLOCK 5
            if objects.block == 'Block 5.0':
                total5 = total5 + 1
                loss5 = loss5 + 1
                rvalueCalc5 = rvalueCalc5 + objects.rvalue
            # BLOCK 6
            if objects.block == 'Block 6.0':
                total6 = total6 + 1
                profit6 = profit6 + 1
                rvalueCalc6 = rvalueCalc6 + objects.rvalue
            # BLOCK 7
            if objects.block == 'Block 7.0':
                total7 = total7 + 1
                un7 = un7 + 1
           # BLOCK 8
            if objects.block == 'Block 8.0':
                total8 = total8 + 1
                un8 = un8 + 1
    # Now I have totals/ It is time to create data frames

    #  First is the data frame carrying all the trades
    # I know the name ref is GAPC and this is GAPFIFTY. To much effort to change frankly
    dfGapcTradeObjects = pandas.DataFrame()
    dfGapcTradeObjects['Pair'] = pairList
    dfGapcTradeObjects['block'] = block
    dfGapcTradeObjects['date'] = date
    dfGapcTradeObjects['profitLoss'] = profitLoss
    dfGapcTradeObjects['rvalue'] = rvalue
    dfGapcTradeObjects['fiftypercentHitPos'] = fiftypercentpos
    dfGapcTradeObjects['halvehittime'] = halvehittime
    dfGapcTradeObjects['fiftypercentvalue'] = fiftypercentvalue
    dfGapcTradeObjects['gapopenvalue'] = gapopenvalue
    dfGapcTradeObjects['tradeopenpos'] = tradeopenpos
    dfGapcTradeObjects['gapFiftyOpenTime'] = gapFiftyOpenTime
    dfGapcTradeObjects['slvalue'] = slvalue
    dfGapcTradeObjects['stoplosstimstr'] = stoplosstimstr
    dfGapcTradeObjects['slpos'] = slpos
    dfGapcTradeObjects['tpvalue'] = tpvalue
    dfGapcTradeObjects['gapfiftytptime'] = gapfiftytptime
    dfGapcTradeObjects['tppos'] = tppos
    dfGapcTradeObjects['comment'] = comment
    dfGapcTradeObjects['Gap Size'] = gapsize
    # Second is the breakdown of block totals
    # Create tupple objects
    def calcrate(profitnum, totalnum):
        if totalnum != 0:
            winrateret = profitnum/totalnum*100
        else:
            winrateret = 0
        return winrateret

    winrateTotal = profit / total * 100
    totalTuple = ('Total', 'Block 1.0', 'Block 2.0', 'Block 3.0', 'Block 4.0', 'Block 5.0', 'Block 6.0', 'Block 7.0', 'Block 8.0')
    winrateTotal1 = calcrate(profit1, total1)
    winrateTotal2 = calcrate(profit2, total2)
    winrateTotal3 = calcrate(profit3, total3)
    winrateTotal4 = calcrate(profit4, total4)
    winrateTotal5 = calcrate(profit5, total5)
    winrateTotal6 = calcrate(profit6, total6)
    winrateTotal7 = calcrate(profit7, total7)
    winrateTotal8 = calcrate(profit8, total8)
    totalTuple1 = (total, total1, total2, total3, total4, total5, total6, total7, total8)
    totalTuple2 = (profit, profit1, profit2, profit3, profit4, profit5, profit6, profit7, profit8)
    totalTuple3 = (loss, loss1, loss2, loss3, loss4, loss5, loss6, loss7, loss8)
    totalTuple4 = (sim, sim1, sim2, sim3, sim4, sim5, sim6, sim7,sim8)
    totalTuple5 = (un, un1, un2, un3, un4, un5, un6, un7,un8)
    totalTuple6 = (rvalueCalc, rvalueCalc1, rvalueCalc2, rvalueCalc3, rvalueCalc4, rvalueCalc5, rvalueCalc6, rvalueCalc7,rvalueCalc8)
    totalTuple7 = (winrateTotal, winrateTotal1, winrateTotal2, winrateTotal3, winrateTotal4, winrateTotal5, winrateTotal6, winrateTotal7, winrateTotal7)


    # winrateTotal = profit/total*100
    # totalTuple = ('Total',total,profit,loss,sim,un,rvalueCalc,winrateTotal)
    # winrateTotal1 = calcrate(profit1,total1)
    # totalTuple1 = ('Block 1.0', total1, profit1, loss1, sim1, un1, rvalueCalc1, winrateTotal1)
    # winrateTotal2 = calcrate(profit2,total2)
    # totalTuple2 = ('Block 2.0', total2, profit2, loss2, sim2, un2, rvalueCalc2, winrateTotal2)
    # winrateTotal3 = calcrate(profit3,total3)
    # totalTuple3 = ('Block 3.0', total3, profit3, loss3, sim3, un3, rvalueCalc3, winrateTotal3)
    # winrateTotal4 = calcrate(profit4,total4)
    # totalTuple4 = ('Block 4.0', total4, profit4, loss4, sim4, un4, rvalueCalc4, winrateTotal4)
    # winrateTotal5 = calcrate(profit5,total5)
    # totalTuple5 = ('Block 5.0', total5, profit5, loss5, sim5, un5, rvalueCalc5, winrateTotal5)
    # winrateTotal6 = calcrate(profit6,total6)
    # totalTuple6 = ('Block 6.0', total6, profit6, loss6, sim6, un6, rvalueCalc6, winrateTotal6)
    # winrateTotal7 = calcrate(profit7,total7)
    # totalTuple7 = ('Block 7.0', total7, profit7, loss7, sim7, un7, rvalueCalc7, winrateTotal7)
    # winrateTotal8 = calcrate(profit8,total8)
    # totalTuple8 = ('Block 8.0', total8, profit8, loss8, sim8, un8, rvalueCalc8, winrateTotal8)
    data_tuples = list(zip(totalTuple, totalTuple1,totalTuple2,totalTuple3,totalTuple4,totalTuple5,totalTuple6,totalTuple7))
    totalsDf = pandas.DataFrame(data_tuples, columns=['Name','Total','Profit','Loss','Sim','Un','R-value','Win Rate %'])
    print(totalsDf)
    return(totalsDf,dfGapcTradeObjects)











