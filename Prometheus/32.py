import sys

x = int(sys.argv[1])
a = 0
b = 1
for i in range(x):
    x = b
    b = a+b 
    a = x
print a
