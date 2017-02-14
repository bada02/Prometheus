import sys
a = sys.argv[1:len(sys.argv)]
u=''
for i in a: 
    x=str(i)
    u=u+x
u=str(u)
z=u.upper()
z.replace(" ","")
q = list(z)
w = list(z)
q.reverse()
if q == w:
    print 'YES'
else:
    print 'NO'
