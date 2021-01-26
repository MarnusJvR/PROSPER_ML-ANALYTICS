import pandas
from Functions import dataProcess
from datetime import date
from datetime import datetime
import datetime
import numpy
import csv
import os.path

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


# Start writing the the final analytics report
# Each file must be called inside the write method
with open('consolodatedGap.csv','w', newline='') as file:
    writer = csv.writer(file)
    specialTupple = dataProcess.readDataframe('CADCHF')
    # writer.writerows(specialTupple)
    print(specialTupple[1])



