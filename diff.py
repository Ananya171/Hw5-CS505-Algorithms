
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
    lcs = [0] * (index)     #stores line numbers of LCS elements in file 1
    lcs2 = [0] * (index)    #stores line numbers of LCS elements in file 2
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = i 
            lcs2[index-1] = j
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    return lcs,lcs2


L1=[]
L2=[]
filename_1=sys.argv[-2]
filename_2=sys.argv[-1]
f=open(filename_1, "r")
g=open(filename_2,"r")
i=1
j=1
for x in f:
    L1.append(hash10(x))
    i=i+1

for y in g:
    L2.append(hash10(y))
    j=j+1

z1,z2=lcs(L1,L2,i-1,j-1)

#print output appropriately
for i in z1:
    print(i,end=" ")
print("\n",end="")
for j in z2:
    print(j,end=" ")





