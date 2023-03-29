import sys
input = sys.stdin.readline

TC = int(input())

for T in range(TC):
    n = int(input())
    people = [0]* (n+1)
    for i in range(n):
        a,b = map(int,input().split())
        people[a]= b

    now = people[1]
    ans = 1
    for i in range(1,n+1):
        if now > people[i]:
            now = people[i]
            ans += 1
    
    print(ans)