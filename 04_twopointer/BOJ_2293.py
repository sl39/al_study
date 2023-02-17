# n, k = map(int,input().split())
# coins = []
# for i in range(n):
#     coins.append(int(input()))
# coins.sort()
# c = max(coins)
# step = [0] * (k+1+c)
# for i in range(1,k+c+1):
#     for j in coins:
#         if i%j == 0:
#             step[i] += 1

# print(step)



TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    print(f"#{T}",end = " ")
    for i in range(int(n**(1/3))+2):
        if i**3 == n:
            print(i)
            break
    else:
        print(-1)
