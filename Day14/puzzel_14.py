map = [x for x in open('input14.txt').read().split('\n')]
#print (map)
mask = {}
cnt = 0

mems = []
master = []
for x in map:
   if x.startswith('mask'):
      mask[cnt] = list(x.split("=")[1].strip())
      cnt = cnt + 1
      if mems:
          master.append(mems)
          mems = []
   else:
       locid = x.split("=")
       #print (locid)
       bitid = list(bin(int(locid[1].strip())))
       tmpl = ['0'] * (36 - (len(bitid) - 2))
       tmpl.extend(bitid[2:])
       mems.append([locid[0].strip(),tmpl])
master.append(mems)

newdic = {}
def calcbit(mask, mem, dick):
    #print (mem)
    for x in range(0,35):
        if dick in newdic:
            if mem[x] == '0' or mem[x] == '1':
                #print (newdic[dick])
                newdic[dick][x] = mem[x]
        if mask[x] == '0' or mask[x]=='1':
            mem[x]= mask[x]
    return mem

cnt = 0

for x in master:
    for m in x:
        new = calcbit(mask[cnt],m[1],m[0])
        newdic[m[0]] = new
        print (new)
        print ("----------")
    cnt = cnt + 1

sum = 0
cnt = 0
for x in newdic:
    #print (x, newdic[x])
    #print ("".join(newdic[x]))
    sum = sum + int("".join(newdic[x]), 2)
    cnt  = cnt+1
print (cnt)
print (sum)
