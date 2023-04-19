import sys
input = sys.stdin.readline

n= int(input())

arr = [0]* (n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    arr[a] += 1
    arr[b] += 1



m = int(input())
for i in range(m):
    t, k = map(int,input().split())
    if t == 2:
        print('yes')
    else:
        if arr[k] >= 2:
            print('yes')
        else:
            print('no')
        



