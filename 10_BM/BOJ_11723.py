import sys
input = sys.stdin.readline

n = int(input())

S = set()

def sett(a,b):
    global visited
    if a == "add":
        visited[int(b)] = 1

    if a == "check":
        if visited[int(b)]:
            print(1)
        else:
            print(0)
    
    if a == 'remove':
        visited[int(b)] = 0
    
    if a =="toggle":
        if visited[int(b)]:
            visited[int(b)] = 0
        else:
            visited[int(b)] = 1
    
    if a == 'all':
        visited = [1] * 21
    
    if a == 'empty':
        visited = [0] * 21
        
visited = [0]*21        
for i in range(n):
    arr = input().split()
    
    if len(arr) == 1:
        sett(arr[0],0)
    else:
        
        sett(arr[0],arr[1])