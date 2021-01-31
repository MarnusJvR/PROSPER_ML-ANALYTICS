import pandas

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
        if objects.profitLoss == 'Profit':
            profit = profit + 1
            rvalueCalc = rvalueCalc + objects.rvalue
        if objects.profitLoss == 'Loss':
            loss = loss + 1
            rvalueCalc = rvalueCalc + objects.rvalue
        if objects.profitLoss == 'SIM':
            sim = sim + 1
        if objects.profitLoss == 'Undetermined':
            un = un + 1
        total = total + 1
        if objects.block == 'Block 1.0':
            total1 = total1 + 1
        if objects.block == 'Block 1.0' and objects.profitLoss == 'Profit':
            profit1 = profit1 + 1
            rvalueCalc1 = rvalueCalc1 + objects.rvalue
        if objects.block == 'Block 1.0' and objects.profitLoss == 'loss':
            loss1 = loss1 + 1
            rvalueCalc1 = rvalueCalc1 + objects.rvalue
        if objects.block == 'Block 1.0' and objects.profitLoss == 'SIM':
            sim1 = sim1 + 1
        if objects.block == 'Block 1.0' and objects.profitLoss == 'Undetermined':
            un1 = un1 + 1
        # BLOCK 2
        if objects.block == 'Block 2.0':
            total2 = total2 + 1
        if objects.block == 'Block 2.0' and objects.profitLoss == 'Profit':
            profit2 = profit2 + 1
            rvalueCalc2 = rvalueCalc2 + objects.rvalue
        if objects.block == 'Block 2.0' and objects.profitLoss == 'loss':
            loss2 = loss2 + 1
            rvalueCalc2 = rvalueCalc2 + objects.rvalue
        if objects.block == 'Block 2.0' and objects.profitLoss == 'SIM':
            sim2 = sim2 + 1
        if objects.block == 'Block 2.0' and objects.profitLoss == 'Undetermined':
            un2 = un2 + 1
        # BLOCK 3
        if objects.block == 'Block 3.0':
            total3 = total3 + 1
        if objects.block == 'Block 3.0' and objects.profitLoss == 'Profit':
            profit3 = profit3 + 1
            rvalueCalc3 = rvalueCalc3 + objects.rvalue
        if objects.block == 'Block 3.0' and objects.profitLoss == 'loss':
            loss3 = loss3 + 1
            rvalueCalc3 = rvalueCalc3 + objects.rvalue
        if objects.block == 'Block 3.0' and objects.profitLoss == 'SIM':
            sim3 = sim3 + 1
        if objects.block == 'Block 3.0' and objects.profitLoss == 'Undetermined':
            un3 = un3 + 1
        # BLOCK 4
        if objects.block == 'Block 4.0':
            total3 = total3 + 1
        if objects.block == 'Block 4.0' and objects.profitLoss == 'Profit':
            profit4 = profit4 + 1
            rvalueCalc4 = rvalueCalc4 + objects.rvalue
        if objects.block == 'Block 4.0' and objects.profitLoss == 'loss':
            loss4 = loss4 + 1
            rvalueCalc4 = rvalueCalc4 + objects.rvalue
        if objects.block == 'Block 4.0' and objects.profitLoss == 'SIM':
            sim4 = sim4 + 1
        if objects.block == 'Block 4.0' and objects.profitLoss == 'Undetermined':
            un4 = un4 + 1
        # BLOCK 5
        if objects.block == 'Block 5.0':
            total5 = total5 + 1
        if objects.block == 'Block 5.0' and objects.profitLoss == 'Profit':
            profit5 = profit5 + 1
            rvalueCalc5 = rvalueCalc5 + objects.rvalue
        if objects.block == 'Block 5.0' and objects.profitLoss == 'loss':
            loss5 = loss5 + 1
            rvalueCalc5 = rvalueCalc5 + objects.rvalue
        if objects.block == 'Block 5.0' and objects.profitLoss == 'SIM':
            sim5 = sim5 + 1
        if objects.block == 'Block 5.0' and objects.profitLoss == 'Undetermined':
            un5 = un5 + 1
        # BLOCK 6
        if objects.block == 'Block 6.0':
            total6 = total6 + 1
        if objects.block == 'Block 6.0' and objects.profitLoss == 'Profit':
            profit6 = profit6 + 1
            rvalueCalc6 = rvalueCalc6 + objects.rvalue
        if objects.block == 'Block 6.0' and objects.profitLoss == 'loss':
            loss6 = loss6 + 1
            rvalueCalc6 = rvalueCalc6 + objects.rvalue
        if objects.block == 'Block 6.0' and objects.profitLoss == 'SIM':
            sim6 = sim6 + 1
        if objects.block == 'Block 6.0' and objects.profitLoss == 'Undetermined':
            un6 = un6 + 1
        # BLOCK 7
        if objects.block == 'Block 7.0':
            total7 = total7 + 1
        if objects.block == 'Block 7.0' and objects.profitLoss == 'Profit':
            profit7 = profit7 + 1
            rvalueCalc7 = rvalueCalc7 + objects.rvalue
        if objects.block == 'Block 7.0' and objects.profitLoss == 'loss':
            loss7 = loss7 + 1
            rvalueCalc7 = rvalueCalc7 + objects.rvalue
        if objects.block == 'Block 7.0' and objects.profitLoss == 'SIM':
            sim7 = sim7 + 1
        if objects.block == 'Block 7.0' and objects.profitLoss == 'Undetermined':
            un7 = un7 + 1
       # BLOCK 7
        if objects.block == 'Block 8.0':
            total8 = total8 + 1
        if objects.block == 'Block 7.0' and objects.profitLoss == 'Profit':
            profit8 = profit8 + 1
            rvalueCalc8 = rvalueCalc8 + objects.rvalue
        if objects.block == 'Block 8.0' and objects.profitLoss == 'loss':
            loss8 = loss8 + 1
            rvalueCalc8 = rvalueCalc8 + objects.rvalue
        if objects.block == 'Block 8.0' and objects.profitLoss == 'SIM':
            sim8 = sim8 + 1
        if objects.block == 'Block 8.0' and objects.profitLoss == 'Undetermined':
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
    # Second is the breakdown of block totals
    # Create tupple objects
    winrateTotal = profit/total*100
    totalTuple = ('Total',total,profit,loss,sim,un,rvalueCalc,winrateTotal)
    winrateTotal1 = profit1 / total1 * 100
    totalTuple1 = ('Block 1.0', total1, profit1, loss1, sim1, un1, rvalueCalc1, winrateTotal1)
    winrateTotal2 = profit2 / total2 * 100
    totalTuple2 = ('Block 2.0', total2, profit2, loss2, sim2, un2, rvalueCalc2, winrateTotal2)
    winrateTotal3 = profit3 / total3 * 100
    totalTuple3 = ('Block 3.0', total3, profit3, loss3, sim3, un3, rvalueCalc3, winrateTotal3)
    winrateTotal4 = profit4 / total4 * 100
    totalTuple4 = ('Block 4.0', total4, profit4, loss4, sim4, un4, rvalueCalc4, winrateTotal4)
    winrateTotal5 = profit5 / total5 * 100
    totalTuple5 = ('Block 5.0', total5, profit5, loss5, sim5, un5, rvalueCalc5, winrateTotal5)
    winrateTotal6 = profit6 / total6 * 100
    totalTuple6 = ('Block 6.0', total6, profit6, loss6, sim6, un6, rvalueCalc6, winrateTotal6)
    winrateTotal7 = profit7 / total7 * 100
    totalTuple7 = ('Block 7.0', total7, profit7, loss7, sim7, un7, rvalueCalc7, winrateTotal7)
    winrateTotal8 = profit8 / total8 * 100
    totalTuple8 = ('Block 8.0', total8, profit8, loss8, sim8, un8, rvalueCalc8, winrateTotal8)
    data_tuples = list(zip(totalTuple, totalTuple1,totalTuple2,totalTuple3,totalTuple4,totalTuple5,totalTuple6,totalTuple7,totalTuple8))
    totalsDf = pandas.DataFrame(data_tuples, columns=['Name','Total','Profit','Loss','Sim','Un','R-value','Win Rate %'])
    return(totalsDf,dfGapcTradeObjects)













