def gapcDataFrameCreator(tradeobjectlist):
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
    for objects in tradeobjectlist:
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
        if objects.profitLoss == 'Profit':
            profit = profit + 1
        if objects.profitLoss == 'Loss':
            loss = loss + 1
        if objects.profitLoss == 'SIM':
            sim = sim + 1
        if objects.profitLoss == 'Undetermined':
            un = un + 1
        total = total + 1
        if objects.block == 'Block 1.0':
            total1 = total1 + 1
        if objects.block == 'Block 1.0' and objects.profitLoss == 'Profit':
            profit1 = profit1 + 1
        if objects.block == 'Block 1.0' and objects.profitLoss == 'loss':
            loss1 = loss1 + 1
        if objects.block == 'Block 1.0' and objects.profitLoss == 'SIM':
            sim1 = sim1 + 1
        if objects.block == 'Block 1.0' and objects.profitLoss == 'Undetermined':
            un1 = un1 + 1








