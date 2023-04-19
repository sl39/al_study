import sys
sys.setrecursionlimit(10**9)


node = []
while True:
    try:
        node.append(int(input()))
    except:
        break

def dfs(first,end):
    if first > end:
        return
    
    mid  = end + 1
    for i in range(first+1,end+1):
        if node[first] < node[i]:
            mid = i
            break
    dfs(first+1,mid-1)
    dfs(mid,end)
    print(node[first])

dfs(0,len(node)-1)