n = int(input())
arr = list(input().split())
p, m = map(int,input().split())
key = [0]*(p)
for i in range(p):
    pare = list(map(int,input().split()))
    start = arr[pare[0]-1]
    for j in range(1,m):
        if start == "W" and arr[pare[j]-1] == "W":
            start = "W"
        else:
            start = "P"
    key[i] = start

start = key[0]

for i in range(1,p):
    if start == "P" and key[i] == "P":
        start = "P"
    else:
        start = "W"
print(start)