class gapcTradeObjects:
    def __init__(self,
                 block,
                 name,
                 date,
                 profitLoss,
                 rvalue,
                 gapclosepos,
                 gapcopenpos,
                 tpvalue,
                 slvalue,
                 tppos,
                 slpos,
                 gapclosetime,
                 gapcopentime,
                 takeprofittime,
                 stoplossstime,
                 comment):
        self.block = block
        self.name = name
        self.date = date
        self.profitloss = profitLoss
        self.rvalue = rvalue
        self.gapclosepos = gapclosepos
        self.gapcopenpos = gapcopenpos
        self.tpvalue = tpvalue
        self.slvalue = slvalue
        self.tppos = tppos
        self.slpos = slpos
        self.gapclosetime = gapclosetime
        self.gapcopentime = gapcopentime
        self.takeprofittime = takeprofittime
        self.stoplossstime = stoplossstime
        self.comment = comment


class gapfiftyTradeObjects:
    def __init__(self,
                 block,
                 name,
                 date,
                 profitLoss,
                 rvalue,
                 fiftypercentvalue,
                 fiftypercentpos,
                 gapopenvalue,
                 tradeopenpos,
                 slvalue,
                 tpvalue,
                 slpos,
                 tppos,
                 gapfiftytptime,
                 gapFiftyOpenTime,
                 halvehittime,
                 stoplosstimstr,
                 comment):
        self.block = block
        self.name = name
        self.date = date
        self.profitloss = profitLoss
        self.rvalue = rvalue
        self.fiftypercentvalue = fiftypercentvalue
        self.fiftypercentpos = fiftypercentpos
        self.gapopenvalue = gapopenvalue
        self.tradeopenpos = tradeopenpos
        self.slvalue = slvalue
        self.tpvalue = tpvalue
        self.slpos = slpos
        self.tppos = tppos
        self.gapfiftytptime = gapfiftytptime
        self.gapFiftyOpenTime =gapFiftyOpenTime
        self.halvehittime = halvehittime
        self.stoplosstimstr = stoplosstimstr
        self.comment = comment


class ftowobjectcreator:
    def __init__(self,
                 block,
                 name,
                 date,
                 profitLoss,
                 rvalue,
                 openvalue,
                 openposition,
                 opentime,
                 TPvalue,
                 TPposition,
                 TPtime,
                 SLvalue,
                 SLpos,
                 SLtime,
                 comment):
        self.block = block
        self.name = name
        self.date = date
        self.profitloss = profitLoss
        self.rvalue = rvalue
        self.openvalue = openvalue
        self.openposition = openposition
        self.opentime = opentime
        self.TPvalue = TPvalue
        self.TPposition = TPposition
        self.TPtime = TPtime
        self.SLvalue = SLvalue
        self.SLpos = SLpos
        self.SLtime = SLtime
        self.comment = comment