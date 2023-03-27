n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    