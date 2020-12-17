input_f = "input16.txt"
f=open(input_f,"r")
wholetxt = f.readlines()
f.close()
wholetxt = [line for line in wholetxt if line.strip()]
ranges = []
yourt = False
rangl = True
nearb = False
nearlis = []
for x in wholetxt:
    if x.startswith("your ticket"):
        yourt = True
        rangl = False
    if rangl:
        b = x.split(":")[1].split("or")
        rang1 = b[0].strip().split("-")
        rang2 = b[1].strip().split("-")
        #print (rang1, rang2)
        ranges.append(list(map(int, rang1)))
        ranges.append(list(map(int, rang2)))
    if nearb:
        nearlis.append([int(x) for x in x.split(",")])
    if x.startswith("nearby tickets"):
        nearb = True

print (ranges)
print (nearlis)

def check_validity(val):
    res = False
    for r in ranges:
        if r[0] <= val <= r[1]:
            res = True
    return res

count = 0
for x in nearlis:
    for row in x:
        #print (row, check_validity(row))
        if not check_validity(row):
            count = count + row
print ("Part 1", count)
