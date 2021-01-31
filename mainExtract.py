import pandas
import sys
from Functions import dataProcess
from datetime import date
from datetime import datetime
import datetime
# import numpy
import csv
import numpy as np
import os.path
from tkinter import *
# import tkinter as tk

# ----GIT---
# echo "# PROSPER_ML-ANALYTICS" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/MarnusJvR/PROSPER_ML-ANALYTICS.git
# git push -u origin main
#

# STRATEGIES: GAPFIFTY
# On price gap (difference in price level between monday opening and friday closing)
# Price must go to 50% gap value to show attempt to close gap, buy then fail and return to gap open
# Trade is opened as price moves through gap open
# Stop loss is set at 15pips
# Take profit is set at 2R

# STRATEGIES: GAPC
# On price gap (difference in price level between monday opening and friday closing)
# Price must close the gap then return to 50%
# Trade is opened as price moves back through 50% value
# Stop loss is set at 15pips
# Take profit is set at 2R




# mainExtract creates consolodated report
# mainExtract -> sends individual CSV file read requests to Functions/dataProcess.py to linearly process each individual csv


# root = Tk()
# root.geometry('580x250')
#
# dates = pandas.date_range('20210101', periods=8)
# dframe = pandas.DataFrame(np.random.randn(8,4),index=dates,columns=list('ABCD'))
#
# txt = Text(root)
# txt.pack()
#
# class PrintToTXT(object):
#  def write(self, s):
#      txt.insert(END, s)
#
# sys.stdout = PrintToTXT()
#
# print('Pandas date range of 8 values in 1 timestamp column adjacent to a numpy random float array of 8 rows and 4 columns, displayed in a Tkinter table')
#
# print(dframe)
#
# mainloop()

dfGapcTotals, dfGapcTradeObjects,dfGapFiftyTotals, dfGapFiftyTradeObjects = dataProcess.readDataframe('AUDJPY')
dfGapcTotals.to_csv('AUDJPY/dfGapcTotals.csv')
dfGapcTotalsCor = dfGapcTotals.corr()
dfGapcTotalsCor.to_csv('AUDJPY/COR/dfGapcTotalsCor.csv')
dfGapcTradeObjects.to_csv('AUDJPY/dfGapcTradeObjects.csv')
dfGapcTradeObjectsCor = dfGapcTradeObjects.corr()
dfGapcTradeObjectsCor.to_csv('AUDJPY/COR/dfGapcTradeObjectsCor.csv')
dfGapFiftyTotals.to_csv('AUDJPY/dfGapFiftyTotals.csv')
dfGapFiftyTotalsCor = dfGapFiftyTotals.corr()
dfGapFiftyTotalsCor.to_csv('AUDJPY/COR/dfGapFiftyTotalsCor.csv')
dfGapFiftyTradeObjects.to_csv('AUDJPY/dfGapFiftyTradeObjects.csv')
dfGapFiftyTradeObjectsCor = dfGapFiftyTradeObjects.corr()
dfGapFiftyTradeObjectsCor.to_csv('AUDJPY/COR/dfGapFiftyTradeObjectsCor.csv')


root = Tk()
root.geometry('1700x1500')


txt = Text(root)
txt.pack()

class PrintToTXT(object):
 def write(self, s):
     txt.insert(END, s)

sys.stdout = PrintToTXT()

print('dfGapcTotals')
print(dfGapcTotals)
print('dfGapcTotalsCor')
print(dfGapcTotalsCor)
print('dfGapcTradeObjects')
print(dfGapcTradeObjects)
print('dfGapcTradeObjectsCor')
print(dfGapcTradeObjectsCor)


mainloop()





root = Tk()
root.geometry('700x500')


txt = Text(root)
txt.pack()

class PrintToTXT(object):
 def write(self, s):
     txt.insert(END, s)

sys.stdout = PrintToTXT()


print('dfGapFiftyTotals')
print(dfGapFiftyTotals)
print('dfGapFiftyTotals')
print(dfGapFiftyTotalsCor)
print('dfGapFiftyTradeObjects')
print(dfGapFiftyTradeObjects)
print('dfGapFiftyTradeObjectsCOR')
print(dfGapFiftyTradeObjectsCor)



mainloop()




