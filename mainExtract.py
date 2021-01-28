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


root = Tk()
root.geometry('580x250')

dates = pandas.date_range('20210101', periods=8)
dframe = pandas.DataFrame(np.random.randn(8,4),index=dates,columns=list('ABCD'))

txt = Text(root)
txt.pack()

class PrintToTXT(object):
 def write(self, s):
     txt.insert(END, s)

sys.stdout = PrintToTXT()

print('Pandas date range of 8 values in 1 timestamp column adjacent to a numpy random float array of 8 rows and 4 columns, displayed in a Tkinter table')

print(dframe)

mainloop()














# import tkinter as tk
#
# def show_entry_fields():
#     print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#     e1.delete(0, tk.END)
#     e2.delete(0, tk.END)
#
# master = tk.Tk()
# tk.Label(master, text="First Name").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)
#
# e1 = tk.Entry(master)
# e2 = tk.Entry(master)
# e1.insert(10, "Miller")
# e2.insert(10, "Jill")
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
#
# tk.Button(master,
#           text='Quit',
#           command=master.quit).grid(row=3,
#                                     column=0,
#                                     sticky=tk.W,
#                                     pady=4)
# tk.Button(master, text='Show', command=show_entry_fields).grid(row=3,
#                                                                column=1,
#                                                                sticky=tk.W,
#                                                                pady=4)
#
# master.mainloop()
#
# tk.mainloop()


# Start by creating homescreen
# mainscreen = tk.Tk()


# def runScript():
#     stoploss = int(edtStopLoss_value.get())
#     pair = edtPair_value.get()
#     gapcObjects, gapFiftyObjects = dataProcess.readDataframe(pair)
#     resultDisplay.insert(END, pair)
#
#
#
#
#
#
# b1= Button(mainscreen, text = 'Execute', command = runScript )
# b1.grid(row=0, column=0,)
#
# t1=Text(mainscreen, height=1, width=20, )
# t1.grid(row=1, column=1)
# edtStopLoss_value = StringVar()
# edtstoploss= Entry(mainscreen, textvariable=edtStopLoss_value)
# edtstoploss.grid(row=1,column=2)
#
# t1=Text(mainscreen, height=1, width=20, )
# t1.grid(row=2, column=1)
# edtPair_value = StringVar()
# edtPair= Entry(mainscreen, textvariable=edtPair_value)
# edtPair.grid(row=2,column=2)
#
# resultDisplay = Text(mainscreen, heigh=2, width=200)
# resultDisplay.grid(row=3,column=0)
#
# mainscreen.mainloop()



# Start writing the the final analytics report
# Each file must be called inside the write method
# with open('consolodatedGap.csv','w', newline='') as file:
#     writer = csv.writer(file)
#     specialTupple = dataProcess.readDataframe('CADCHF')
    # writer.writerows(specialTupple)
    # print(specialTupple[1])



