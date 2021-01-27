# function ndentifies weekend gap
# all lists recieved from DF2
# recieves all the variable named below. Dont be lazy just read.

def gapIdentifyer(pair, gapsizes, mydate, gapsizenumber, negativegapsizenumber):
    print('GAPFIFTYID verifyer call received')
    count = 0
    gapindetifyer = []
    if pair == 'DE3030' or pair == 'US3030':
        for nums in gapsizes:
            date2 = mydate[count]
            year = date2.year
            prevdate = mydate[count - 1]
            newdate = date2 - prevdate
            if year >= 2015:
                if newdate.days == 3:
                    if nums >= gapsizenumber or nums <= negativegapsizenumber:
                        gapindetifyer.append("GAP")
                    else:
                        gapindetifyer.append("NONE")
                else:
                    gapindetifyer.append("NONE")
            else:
                gapindetifyer.append('NONE')
            count += 1
    else:
        for nums in gapsizes:
            date2 = mydate[count]
            prevdate = mydate[count - 1]
            newdate = date2 - prevdate
            if newdate.days == 3:
                if nums >= gapsizenumber or nums <= negativegapsizenumber:
                    gapindetifyer.append("GAP")
                else:
                    gapindetifyer.append("NONE")
            else:
                gapindetifyer.append("NONE")
            count += 1
    return gapindetifyer
