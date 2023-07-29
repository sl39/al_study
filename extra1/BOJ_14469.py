n = int(input())
arr = []
for i in range(n):
    start, t = map(int,input().split())
    arr.append((start,t))
arr.sort()
answer = 0
for i in arr:
    if answer >= i[0]:
        answer += i[1]
    else:
        answer = i[0] + i[1]
print(answer)