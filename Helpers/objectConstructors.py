class gapcTradeObjects:
    def __init__(self,
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
                 stoplossstime):
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


class gapfiftyTradeObjects:
    def __init__(self,
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
