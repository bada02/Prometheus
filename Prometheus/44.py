import sys
q=[] # initial list
y=[] # string list full
p=0
a = int(sys.argv[1]) # 1 limit
b = int(sys.argv[2]) # 2 limit
res=0      # resultant answer
z=a
while z<=b: # forming initial list within range ab
    q.append(z)
    z=z+1
for i in q: # checking list element length
    x=str(i)
    while len(x)<6: # adding 0 to list elements having length < 6
        x='0'+x
    xlist=list(x)   # forming correct list
    for i in xlist: # converting list elements to int for calculation
        xi=int(float(xlist[int(float(p))]))
        p=p+1
        y.append(xi)
    if sum(y[:3])==sum(y[3:]): # checking lucky condition
        res=res+1            # calculating quantity of lucky tickets in given range ab
    y=[]
    p=0
print res
