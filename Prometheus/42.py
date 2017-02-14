import sys
t=0
d=0
a=""
li=sys.argv[1:len(sys.argv)]
li.reverse()
for x in li:
   a = a + x + ' '
print a[:len(a)-1]
