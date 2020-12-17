map = [x for x in open('input13.txt').read().split('\n')]
print (map)
busid = []
intg = 0
cntr = 0
mainc = 0
for j in map[1].split(","):
    if j.isdigit():
        intg = int(j)
        cntr = mainc
        busid.append([intg,cntr])
    if j=='x':
        cntr = cntr+1
    mainc = mainc + 1

def checkdep():
    tot = 10000000000000
    tot = 10004734683664
    tot = 20234252392161
    tot = 22609006213611
    tot = 40468504784321
    tot = 31112961906486
    tot = 52609056219590
    log=[False]
    while not all(log):
        tot = tot + busid[0][0]
        log = []
        #[ x if x%2 else x*100 for x in range(1, 10) ]
        [log.append(True) if (tot + busid[x][1]) % busid[x][0] == 0 else log.append(False) for x in range(1,len(busid))]
        #for x in range(1,len(busid)):
        #    if (tot + busid[x][1])% busid[x][0] == 0:
        #        print (tot, busid[x][1])
        #        log.append(True)
        #    else:
        #        log.append(False)
        print (tot, log)
    print (tot)


print (busid)
checkdep()