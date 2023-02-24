import sys
input = sys.stdin.readline

n = int(input())
arr = [0] *(1000001)
for i in range(n):
    num = int(input())
    arr[num] = 1

for i in range(1000001):
    if arr[i]:
        print(i)
