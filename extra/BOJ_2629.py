import sys
input = sys.stdin.readline

n = int(input())
chu = list(map(int,input().split()))
m = int(input())
marble = list(map(int,input().split()))

g = [[0]*(500*30+1) for i in range(n+1)]

visited= []

def dfs(now,res):
    global visited
    if not res in visited:
        visited.append(res)

    if g[now-1][res] == 1:
        return
    
    if now == n:
        return
    
    g[now-1][res] = 1

    dfs(now+1,res+chu[now])
    dfs(now+1,res)
    dfs(now+1,abs(res-chu[now]))

dfs(0,0)

for i in marble:
    if i in visited:
        print("Y", end=" ")
    else:
        print("N", end=" ")
print()