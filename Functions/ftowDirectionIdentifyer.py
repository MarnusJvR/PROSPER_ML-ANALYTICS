def directionidentifyer(mydate, downhitpos, uphitpos, uphittime, downhittime):
    # TODO: I must still add the logic that stops positive if negative is triggired ect
    print(' FTOW direction tracker received')
    counter = 0
    directionid = []
    openpos = []
    opentime = []
    for dates in mydate:
        # Monday= 0 Tuesday = 1 Wednesday = 2 Thursday = 3 Friday = 4
        # We want closing on 4 ! opening on 0 ? !
        # If positive is triggered then negative is deactivated
        weekday = dates.weekday()
        if weekday == 0:
            # check what was hit first
            if uphitpos[counter] != 'NONE' and downhitpos[counter] != 'NONE':
                if uphitpos[counter] > downhitpos[counter]:
                    directionid.append('Positive')
                    openpos.append(uphitpos[counter])
                    opentime.append(uphittime[counter])
                elif uphitpos[counter] < downhitpos[counter]:
                    directionid.append('Negative')
                    openpos.append(downhitpos[counter])
                    opentime.append(downhittime[counter])
                elif uphitpos[counter] == downhitpos[counter]:
                    directionid.append('SIM')
                    openpos.append('NONE')
                    opentime.append('NONE')
                else:
                    print('wtf')
                    directionid.append('wtf')
            if uphitpos[counter] != 'NONE' and downhitpos[counter] == 'NONE':
                directionid.append('Positive')
                openpos.append(uphitpos[counter])
                opentime.append(uphittime[counter])
            if uphitpos[counter] == 'NONE' and downhitpos[counter] != 'NONE':
                directionid.append('Negative')
                openpos.append(downhitpos[counter])
                opentime.append(downhittime[counter])
            if uphitpos[counter] == 'NONE' and downhitpos[counter] == 'NONE':
                directionid.append('NONE')
                openpos.append('NONE')
                opentime.append('NONE')
        else:
            directionid.append('NONE')
            openpos.append('NONE')
            opentime.append('NONE')
        counter = counter + 1
    return directionid,openpos,opentime







