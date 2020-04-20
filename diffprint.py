
import sys
def hash10(s): #to compute hash value that is compressed to 10 bits
    l=hash(s)%1023
    return l

def lcs(X, Y, m, n): 
    # This function was found at https://www.geeksforgeeks.org/printing-longest-common-subsequence/ and modified by us

    L = [[0 for x in range(n+1)] for y in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    index = L[m][n]         #gives length of the longest common subsequence
    lb1 = ["  "] * (m)      #stores prefix of each line for file 1(bonus)
    lb2 = ["  "] * (n)      #stores prefix of each line for file 2

    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        if X[i-1] == Y[j-1]: 
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]: 
            lb1[i-1]="- "
            i-=1
        else: 
            lb2[j-1]="+ "
            j-=1
    if i!=0:  
        lb1[0]="- "
    elif j!=0:
        lb2[0]="+ "
    return lb1,lb2

d1={} #stores line number to line mapping in file 1
d2={} #stores line number to line mapping in file 2
L1=[]
L2=[]
filename_1=sys.argv[-2]
filename_2=sys.argv[-1]
f=open(filename_1, "r")
g=open(filename_2,"r")
i=1
j=1

for x in f:
    d1[i]=x
    L1.append(hash10(x))
    i=i+1
for y in g:
    d2[j]=y
    L2.append(hash10(y))
    j=j+1

y1,y2=lcs(L1,L2,i-1,j-1)

for ind,i in enumerate(y1):
    print(i,d1[ind+1],end="")

for ind,j in enumerate(y2):
    if j!= "  ":
        print(j,d2[ind+1],end="")


