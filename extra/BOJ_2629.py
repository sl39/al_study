n = int(input())
chu = list(map(int,input().split()))
m = int(input())
marble = list(map(int,input().split()))


visited= [[0]*(500*30+1) for i in range(n)]

def dfs(now):
    
