## do you wanna build the snowman~ 
import sys
input = sys.stdin.readline

n = int(input())
snow = list(map(int,input().split()))

snow.sort()
i = 0
mn = 4000000001

for i in range(n-3):
    for j in range(i+3,n):
        a1 = snow[i] + snow[j]
        start = i+1
        end = j-1
        while start < end:
            a2 = snow[start] + snow[end]
            mn = min(mn,abs(a2-a1))
            if a2 > a1:
                end -= 1
            elif a2 < a1:
                start += 1
            else:
                print(0)
                exit()
print(mn)