import sys
x=sys.argv[1]
q=0
a=0
b=0
for i in x:
    c= x[q]
    if c=='(':
            a=a+1
    elif c==')':
            a=a-1
    if a<0:
        b=b-1
    q=q+1
if a==0 and b>=0:
    print 'YES'
else:
    print 'NO'
