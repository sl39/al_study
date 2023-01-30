import math
import sys
input = sys.stdin.readline
N = int(input())
li = []
ls = []
for i in range(N):
    li.append(int(input()))
    if i != 0:
        ls.append(li[i]-li[i-1])
A = math.gcd(*ls)
common = []
for i in range(2,round((A)**1/2) + 1):
    if A % i ==0 :
        common.append(i)
common.append(A)
cl = len(common)
if cl == 1:
    print(common[0])
else:
    for i in range(cl-1):
        print(common[i],end = " ")
    print(common[-1])
