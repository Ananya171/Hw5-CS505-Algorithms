
import sys
def hash10(s): #to compute hash value that is compressed to 10 bits
    l=hash(s)%1023
    return l

filename=sys.argv[-1]
f=open(filename,"r")
for i in f:
    s=hash10(i)
    print(s)