import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
if a>0 and b>0 and c>0 and a+b>c and a+c>b and c+b>a:
    print "triangle"
else :
    print "not triangle"
