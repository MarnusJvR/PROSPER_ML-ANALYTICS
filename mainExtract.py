import pandas
from Functions import dataProcess
from datetime import date
from datetime import datetime
import datetime
import numpy
import csv
import os.path

# ----GIT---
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/MarnusJvR/Finance-Machine-Learning-Analytics-.git
# git push -u origin main


# mainExtract creates consolodated report
# mainExtract -> sends individual CSV file read requests to Functions/dataProcess.py to linearly process each individual csv


# Start writing the the final analytics report
# Each file must be called inside the write method
with open('consolodatedGap.csv','w', newline='') as file:
    writer = csv.writer(file)
    specialTupple = dataProcess.readDataframe('CADCHF')
    # writer.writerows(specialTupple)
    print(specialTupple[1])



