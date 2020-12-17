
input_f = "input15.txt"
f=open(input_f,"r")
wholetxt = f.read()
map = wholetxt.split(",")
lis = []
for x in map:
    lis.append(int(x))
print (map)
count = 2020

def find_prev(cur):
    return [i for i, x in enumerate(lis) if x == lis[cur]]
    print ("Cur",cur)

newval = []
for x in range(0,count):
    if x<len(lis):
        newval.append(lis[x])
    else:
        preind = find_prev(x - 1)
        if len(preind)==2:
            newval.append(preind[len(preind)-1] - preind[0])
            lis.append(preind[len(preind)-1] - preind[0])
        elif len(preind) > 2:
            leng = len(preind)
            newval.append(preind[leng-1] - preind[leng-2])
            lis.append(preind[leng-1] - preind[leng-2])
        else:
            newval.append(0)
            lis.append(0)
#print ("List", newval)
print ("Part1", newval[len(newval)-1])
