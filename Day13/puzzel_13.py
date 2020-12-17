map = [x for x in open('input13.txt').read().split('\n')]
print (map)
nearst = int(map[0])
busid = [int(y) for y in map[1].split(",") if y != 'x']


est =[]
lowst = 0
lo = 0
timestamp = 0
firstp = True
for s in busid:
    nr = (nearst // s)*s
    #est.append(nr)
    if nr<nearst:
       est.append(nr+s)
       nr = nr + s
    if firstp:
        lo = nr - nearst
        firstp = False
    #print ("s ", s)
    if (nr-nearst) < lo:
        #print ((nr-nearst), " - ", lo)
        lo = nr - nearst
        timestamp = nr
        lowst = s

print (lowst)
print ((timestamp - nearst) * lowst)
