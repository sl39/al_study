N, d, k, c  = map(int,input().split())

sushi = []
for i in range(N):
    sushi.append(int(input()))
if k not in sushi:
    sushi.append(k)

