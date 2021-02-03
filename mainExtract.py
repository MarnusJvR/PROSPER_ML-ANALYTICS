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

AUDCADdfGapcTotals, AUDCADdfGapcTradeObjects,AUDCADdfGapFiftyTotals, AUDCADdfGapFiftyTradeObjects = dataProcess.readDataframe('AUDCAD')

AUDCHFdfGapcTotals, AUDCHFdfGapcTradeObjects,AUDCHFdfGapFiftyTotals, AUDCHFdfGapFiftyTradeObjects = dataProcess.readDataframe('AUDCHF')
AUDCHF1dfGapcTotals, AUDCHF1dfGapcTradeObjects,AUDCHF1dfGapFiftyTotals, AUDCHF1dfGapFiftyTradeObjects = dataProcess.readDataframe('AUDCHF1')

AUDJPYdfGapcTotals, AUDJPYdfGapcTradeObjects,AUDJPYdfGapFiftyTotals, AUDJPYdfGapFiftyTradeObjects = dataProcess.readDataframe('AUDJPY')
AUDJPY1dfGapcTotals, AUDJPY1dfGapcTradeObjects,AUDJPY1dfGapFiftyTotals, AUDJPY1dfGapFiftyTradeObjects = dataProcess.readDataframe('AUDJPY1')

AUDNZD1dfGapcTotals, AUDNZD1dfGapcTradeObjects,AUDNZD1dfGapFiftyTotals, AUDNZD1dfGapFiftyTradeObjects = dataProcess.readDataframe('AUDNZD1')

AUDUSDdfGapcTotals, AUDUSDdfGapcTradeObjects,AUDUSDdfGapFiftyTotals, AUDUSDdfGapFiftyTradeObjects = dataProcess.readDataframe('AUDUSD')
AUDUSD1dfGapcTotals, AUDUSD1dfGapcTradeObjects,AUDUSD1dfGapFiftyTotals, AUDUSD1dfGapFiftyTradeObjects = dataProcess.readDataframe('AUDUSD1')

CADCHF_30dfGapcTotals, CADCHF_30dfGapcTradeObjects,CADCHF_30dfGapFiftyTotals, CADCHF_30dfGapFiftyTradeObjects = dataProcess.readDataframe('CADCHF_30')

CADJPYdfGapcTotals, CADJPYdfGapcTradeObjects,CADJPYdfGapFiftyTotals, CADJPYdfGapFiftyTradeObjects = dataProcess.readDataframe('CADJPY')

CHFJPYdfGapcTotals, CHFJPYdfGapcTradeObjects, CHFJPYdfGapFiftyTotals, CHFJPYdfGapFiftyTradeObjects = dataProcess.readDataframe('CHFJPY')
CHFJPY1dfGapcTotals, CHFJPY1dfGapcTradeObjects, CHFJPY1dfGapFiftyTotals, CHFJPY1dfGapFiftyTradeObjects = dataProcess.readDataframe('CHFJPY1')

EURAUDdfGapcTotals, EURAUDdfGapcTradeObjects, EURAUDdfGapFiftyTotals, EURAUDdfGapFiftyTradeObjects = dataProcess.readDataframe('EURAUD')

EURCADdfGapcTotals, EURCADdfGapcTradeObjects,EURCADdfGapFiftyTotals, EURCADdfGapFiftyTradeObjects = dataProcess.readDataframe('EURCAD')

EURCHFdfGapcTotals, EURCHFdfGapcTradeObjects, EURCHFdfGapFiftyTotals, EURCHFdfGapFiftyTradeObjects = dataProcess.readDataframe('EURCHF')
EURCHF1dfGapcTotals, EURCHF1dfGapcTradeObjects, EURCHF1dfGapFiftyTotals, EURCHF1dfGapFiftyTradeObjects = dataProcess.readDataframe('EURCHF1')

EURGBPdfGapcTotals, EURGBPdfGapcTradeObjects, EURGBPdfGapFiftyTotals, EURGBPdfGapFiftyTradeObjects = dataProcess.readDataframe('EURGBP')
EURGBP1dfGapcTotals, EURGBP1dfGapcTradeObjects, EURGBP1dfGapFiftyTotals, EURGBP1dfGapFiftyTradeObjects = dataProcess.readDataframe('EURGBP1')

EURJPY1dfGapcTotals, EURJPY1dfGapcTradeObjects, EURJPY1dfGapFiftyTotals, EURJPY1dfGapFiftyTradeObjects = dataProcess.readDataframe('EURJPY1')

EURNZDdfGapcTotals, EURNZDdfGapcTradeObjects, EURNZDdfGapFiftyTotals, EURNZDdfGapFiftyTradeObjects = dataProcess.readDataframe('EURNZD')
EURNZD1dfGapcTotals, EURNZD1dfGapcTradeObjects, EURNZD1dfGapFiftyTotals, EURNZD1dfGapFiftyTradeObjects = dataProcess.readDataframe('EURNZD1')

EURUSDdfGapcTotals, EURUSDdfGapcTradeObjects, EURUSDdfGapFiftyTotals, EURUSDdfGapFiftyTradeObjects = dataProcess.readDataframe('EURUSD')
EURUSD1dfGapcTotals, EURUSD1dfGapcTradeObjects, EURUSD1dfGapFiftyTotals, EURUSD1dfGapFiftyTradeObjects = dataProcess.readDataframe('EURUSD1')

GBPAUDdfGapcTotals, GBPAUDdfGapcTradeObjects, GBPAUDdfGapFiftyTotals, GBPAUDdfGapFiftyTradeObjects = dataProcess.readDataframe('GBPAUD')
GBPAUD1dfGapcTotals, GBPAUD1dfGapcTradeObjects, GBPAUD1dfGapFiftyTotals, GBPAUD1dfGapFiftyTradeObjects = dataProcess.readDataframe('GBPAUD1')

GBPCADdfGapcTotals, GBPCADdfGapcTradeObjects, GBPCADdfGapFiftyTotals, GBPCADdfGapFiftyTradeObjects = dataProcess.readDataframe('GBPCAD')
GBPCAD1dfGapcTotals, GBPCAD1dfGapcTradeObjects, GBPCAD1dfGapFiftyTotals, GBPCAD1dfGapFiftyTradeObjects = dataProcess.readDataframe('GBPCAD1')

GBPCHFdfGapcTotals, GBPCHFdfGapcTradeObjects,GBPCHFdfGapFiftyTotals, GBPCHFdfGapFiftyTradeObjects = dataProcess.readDataframe('GBPCHF')
GBPCHF1dfGapcTotals, GBPCHF1dfGapcTradeObjects, GBPCHF1dfGapFiftyTotals, GBPCHF1dfGapFiftyTradeObjects = dataProcess.readDataframe('GBPCHF1')

GBPJPYdfGapcTotals, GBPJPYdfGapcTradeObjects, GBPJPYdfGapFiftyTotals, GBPJPYdfGapFiftyTradeObjects = dataProcess.readDataframe('GBPJPY')

GBPNZDdfGapcTotals, GBPNZDdfGapcTradeObjects, GBPNZDdfGapFiftyTotals, GBPNZDdfGapFiftyTradeObjects = dataProcess.readDataframe('GBPNZD')
GBPNZD1dfGapcTotals, GBPNZD1dfGapcTradeObjects, GBPNZD1dfGapFiftyTotals, GBPNZD1dfGapFiftyTradeObjects = dataProcess.readDataframe('GBPNZD1')

GBPNZD1dfGapcTotals, GBPUSDdfGapcTradeObjects, GBPUSDdfGapFiftyTotals, GBPUSDdfGapFiftyTradeObjects = dataProcess.readDataframe('GBPUSD')
GBPUSD1dfGapcTotals, GBPUSD1dfGapcTradeObjects, GBPUSD1dfGapFiftyTotals, GBPUSD1dfGapFiftyTradeObjects = dataProcess.readDataframe('GBPUSD1')

NZDCADdfGapcTotals, NZDCADdfGapcTradeObjects, NZDCADdfGapFiftyTotals, NZDCADdfGapFiftyTradeObjects = dataProcess.readDataframe('NZDCAD')
NZDCAD1dfGapcTotals, NZDCAD1dfGapcTradeObjects, NZDCAD1dfGapFiftyTotals, NZDCAD1dfGapFiftyTradeObjects = dataProcess.readDataframe('NZDCAD1')

NZDCHFdfGapcTotals, NZDCHFdfGapcTradeObjects, NZDCHFdfGapFiftyTotals, NZDCHFdfGapFiftyTradeObjects = dataProcess.readDataframe('NZDCHF')
NZDCHF1dfGapcTotals, NZDCHF1dfGapcTradeObjects, NZDCHF1dfGapFiftyTotals, NZDCHF1dfGapFiftyTradeObjects = dataProcess.readDataframe('NZDCHF1')

NZDJPYdfGapcTotals, NZDJPYdfGapcTradeObjects, NZDJPYdfGapFiftyTotals,NZDJPYdfGapFiftyTradeObjects = dataProcess.readDataframe('NZDJPY')

gapcTradeObjectsFrame = [AUDCADdfGapcTradeObjects,
                         AUDCHFdfGapcTradeObjects,
                         AUDCHF1dfGapcTradeObjects,
                         AUDJPYdfGapcTradeObjects,
                         AUDJPY1dfGapcTradeObjects,
                         AUDNZD1dfGapcTradeObjects,
                         AUDUSDdfGapcTradeObjects,
                         AUDUSD1dfGapcTradeObjects,
                         CADCHF_30dfGapcTradeObjects,
                         CADJPYdfGapcTradeObjects,
                         CHFJPYdfGapcTradeObjects,
                         CHFJPY1dfGapcTradeObjects,
                         EURAUDdfGapcTradeObjects,
                         EURCADdfGapcTradeObjects,
                         EURCHFdfGapcTradeObjects,
                         EURCHF1dfGapcTradeObjects,
                         EURGBPdfGapcTradeObjects,
                         EURGBP1dfGapcTradeObjects,
                         EURJPY1dfGapcTradeObjects,
                         EURNZDdfGapcTradeObjects,
                         EURNZD1dfGapcTradeObjects,
                         EURUSDdfGapcTradeObjects,
                         EURUSD1dfGapcTradeObjects,
                         GBPAUDdfGapcTradeObjects,
                         GBPAUD1dfGapcTradeObjects,
                         GBPCADdfGapcTradeObjects,
                         GBPCAD1dfGapcTradeObjects,
                         GBPCHFdfGapcTradeObjects,
                         GBPCHF1dfGapcTradeObjects,
                         GBPJPYdfGapcTradeObjects,
                         GBPNZDdfGapcTradeObjects,
                         GBPNZD1dfGapcTradeObjects,
                         GBPUSDdfGapcTradeObjects,
                         GBPUSD1dfGapcTradeObjects,
                         NZDCADdfGapcTradeObjects,
                         NZDCAD1dfGapcTradeObjects,
                         NZDCHFdfGapcTradeObjects,
                         NZDCHF1dfGapcTradeObjects,
                         NZDJPYdfGapcTradeObjects]

gapcTradeObjectsPrint = pandas.concat(gapcTradeObjectsFrame)

GapFiftyTradeObjectsFrame = [AUDCADdfGapFiftyTradeObjects,
                             AUDCHFdfGapFiftyTradeObjects,
                             AUDCHF1dfGapFiftyTradeObjects,
                             AUDJPYdfGapFiftyTradeObjects,
                             AUDJPY1dfGapFiftyTradeObjects,
                             AUDNZD1dfGapFiftyTradeObjects,
                             AUDUSDdfGapFiftyTradeObjects,
                             AUDUSD1dfGapFiftyTradeObjects,
                             CADCHF_30dfGapFiftyTradeObjects,
                             CADJPYdfGapFiftyTradeObjects,
                             CHFJPYdfGapFiftyTradeObjects,
                             CHFJPY1dfGapFiftyTradeObjects,
                             EURAUDdfGapFiftyTradeObjects,
                             EURCADdfGapFiftyTradeObjects,
                             EURCHFdfGapFiftyTradeObjects,
                             EURCHF1dfGapFiftyTradeObjects,
                             EURGBPdfGapFiftyTradeObjects,
                             EURGBP1dfGapFiftyTradeObjects,
                             EURJPY1dfGapFiftyTradeObjects,
                             EURNZDdfGapFiftyTradeObjects,
                             EURNZD1dfGapFiftyTradeObjects,
                             EURUSDdfGapFiftyTradeObjects,
                             EURUSD1dfGapFiftyTradeObjects,
                             GBPAUDdfGapFiftyTradeObjects,
                             GBPAUD1dfGapFiftyTradeObjects,
                             GBPCADdfGapFiftyTradeObjects,
                             GBPCAD1dfGapFiftyTradeObjects,
                             GBPCHFdfGapFiftyTradeObjects,
                             GBPCHF1dfGapFiftyTradeObjects,
                             GBPJPYdfGapFiftyTradeObjects,
                             GBPNZDdfGapFiftyTradeObjects,
                             GBPNZD1dfGapFiftyTradeObjects,
                             GBPUSDdfGapFiftyTradeObjects,
                             GBPUSD1dfGapFiftyTradeObjects,
                             NZDCADdfGapFiftyTradeObjects,
                             NZDCAD1dfGapFiftyTradeObjects,
                             NZDCHFdfGapFiftyTradeObjects,
                             NZDCHF1dfGapFiftyTradeObjects,
                             NZDJPYdfGapFiftyTradeObjects]

gapFiftyTradeObjectsPrint = pandas.concat(GapFiftyTradeObjectsFrame)

gapcTotalFrame = [AUDCADdfGapcTotals,
                  AUDCHFdfGapcTotals,
                  AUDCHF1dfGapcTotals,
                  AUDJPYdfGapcTotals,
                  AUDJPY1dfGapcTotals,
                  AUDNZD1dfGapcTotals,
                  AUDUSDdfGapcTotals,
                  AUDUSD1dfGapcTotals,
                  CADCHF_30dfGapcTotals,
                  CADJPYdfGapcTotals,
                  CHFJPYdfGapcTotals,
                  CHFJPY1dfGapcTotals,
                  EURAUDdfGapcTotals,
                  EURCADdfGapcTotals,
                  EURCHFdfGapcTotals,
                  EURCHF1dfGapcTotals,
                  EURGBPdfGapcTotals,
                  EURGBP1dfGapcTotals,
                  EURJPY1dfGapcTotals,
                  EURNZDdfGapcTotals,
                  EURNZD1dfGapcTotals,
                  EURUSDdfGapcTotals,
                  EURUSD1dfGapcTotals,
                  GBPAUDdfGapcTotals,
                  GBPAUD1dfGapcTotals,
                  GBPCADdfGapcTotals,
                  GBPCAD1dfGapcTotals,
                  GBPCHFdfGapcTotals,
                  GBPCHF1dfGapcTotals,
                  GBPJPYdfGapcTotals,
                  GBPNZDdfGapcTotals,
                  GBPNZD1dfGapcTotals,
                  GBPUSD1dfGapcTotals,
                  NZDCADdfGapcTotals,
                  NZDCAD1dfGapcTotals,
                  NZDCHFdfGapcTotals,
                  NZDCHF1dfGapcTotals,
                  NZDJPYdfGapcTotals]

gapcTotalPrint = pandas.concat(gapcTotalFrame)

gapFiftyTotalFrame = [AUDCADdfGapFiftyTotals,
                      AUDCHFdfGapFiftyTotals,
                      AUDCHF1dfGapFiftyTotals,
                      AUDJPYdfGapFiftyTotals,
                      AUDJPY1dfGapFiftyTotals,
                      AUDNZD1dfGapFiftyTotals,
                      AUDUSDdfGapFiftyTotals,
                      AUDUSD1dfGapFiftyTotals,
                      CADCHF_30dfGapFiftyTotals,
                      CADJPYdfGapFiftyTotals,
                      CHFJPYdfGapFiftyTotals,
                      CHFJPY1dfGapFiftyTotals,
                      EURAUDdfGapFiftyTotals,
                      EURCADdfGapFiftyTotals,
                      EURCHFdfGapFiftyTotals,
                      EURCHF1dfGapFiftyTotals,
                      EURGBPdfGapFiftyTotals,
                      EURGBP1dfGapFiftyTotals,
                      EURJPY1dfGapFiftyTotals,
                      EURNZDdfGapFiftyTotals,
                      EURNZD1dfGapFiftyTotals,
                      EURUSDdfGapFiftyTotals,
                      EURUSD1dfGapFiftyTotals,
                      GBPAUDdfGapFiftyTotals,
                      GBPAUD1dfGapFiftyTotals,
                      GBPCADdfGapFiftyTotals,
                      GBPCAD1dfGapFiftyTotals,
                      GBPCHFdfGapFiftyTotals,
                      GBPCHF1dfGapFiftyTotals,
                      GBPJPYdfGapFiftyTotals,
                      GBPNZDdfGapFiftyTotals,
                      GBPNZD1dfGapFiftyTotals,
                      GBPUSD1dfGapFiftyTotals,
                      NZDCADdfGapFiftyTotals,
                      NZDCAD1dfGapFiftyTotals,
                      NZDCHFdfGapFiftyTotals,
                      NZDCHF1dfGapFiftyTotals,
                      NZDJPYdfGapFiftyTotals]


gapFiftyTotalPrint = pandas.concat(gapFiftyTotalFrame)


gapcTradeObjectsPrint.to_csv('RESULTS/gapcTradeObjects.csv')
gapFiftyTradeObjectsPrint.to_csv('RESULTS/gapFiftyTradeObjects.csv')
gapcTotalPrint.to_csv('RESULTS/gapcTotal.csv')
gapFiftyTotalPrint.to_csv('RESULTS/gapFiftyTotal.csv')



# dfGapcTotals.to_csv('RESULTS/AUDJPY1/dfGapcTotals.csv')
# dfGapcTotalsCor = dfGapcTotals.corr()
# dfGapcTotalsCor.to_csv('RESULTS/AUDJPY1/COR/dfGapcTotalsCor.csv')
# dfGapcTradeObjects.to_csv('RESULTS/AUDJPY1/dfGapcTradeObjects.csv')
# dfGapcTradeObjectsCor = dfGapcTradeObjects.corr()
# dfGapcTradeObjectsCor.to_csv('RESULTS/AUDJPY1/COR/dfGapcTradeObjectsCor.csv')
# dfGapFiftyTotals.to_csv('RESULTS/AUDJPY1/dfGapFiftyTotals.csv')
# dfGapFiftyTotalsCor = dfGapFiftyTotals.corr()
# dfGapFiftyTotalsCor.to_csv('RESULTS/AUDJPY1/COR/dfGapFiftyTotalsCor.csv')
# dfGapFiftyTradeObjects.to_csv('RESULTS/AUDJPY1/dfGapFiftyTradeObjects.csv')
# dfGapFiftyTradeObjectsCor = dfGapFiftyTradeObjects.corr()
# dfGapFiftyTradeObjectsCor.to_csv('RESULTS/AUDJPY1/COR/dfGapFiftyTradeObjectsCor.csv')

#
# root = Tk()
# root.geometry('1700x1500')
#
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
# print('dfGapcTotals')
# print(dfGapcTotals)
# print('dfGapcTotalsCor')
# print(dfGapcTotalsCor)
# print('dfGapcTradeObjects')
# print(dfGapcTradeObjects)
# print('dfGapcTradeObjectsCor')
# print(dfGapcTradeObjectsCor)
#
#
# mainloop()
#
#
#
#
#
# root = Tk()
# root.geometry('700x500')
#
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
#
# print('dfGapFiftyTotals')
# print(dfGapFiftyTotals)
# print('dfGapFiftyTotals')
# print(dfGapFiftyTotalsCor)
# print('dfGapFiftyTradeObjects')
# print(dfGapFiftyTradeObjects)
# print('dfGapFiftyTradeObjectsCOR')
# print(dfGapFiftyTradeObjectsCor)
#
#
#
# mainloop()




