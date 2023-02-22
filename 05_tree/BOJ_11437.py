from collections import deque
import sys


input = sys.stdin.readline
n = int(input())
arr = [0] *(n+1)
mat = [[] for i in range(n+1)]
plist = [0] *(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    mat[a].append(b)
    mat[b].append(a)
arr[1] = [1,1]
q = deque([[1,1]])
while q:
    node,depth = q.popleft()
    for i in mat[node]:
        if not arr[i]:
            arr[i] = [node,depth +1]
            q.append([i,depth+1])
    depth += 1


def tree(n1,n2):
    global plist
    if plist[n1]:
        parents1 = plist[n1]
    else:
        parents1 = [n1]
        a = n1
        while a != 1:
            a1 = a
            a,c = arr[a]
            parents1.append((a1,c))
        plist[n1] = parents1
       
    if plist[n2]:
        parents2 = plist[n2]
    else:

        parents2 = [n2]
        b = n2
        while b != 1:
            b1 = b
            b,d = arr[b]
            parents2.append((b1,d))
        plist[n2] = parents2
        

    a = set(parents1) & set(parents2)
    dep = -1
    mx = n+1

    if len(a) == 0:
        return 1
    else:
        for i in a:
            if dep < i[1]:
                dep = i[1]
                
                mx = i[0]
        return mx

m = int(input())
for i in range(m):
    n1,n2 = map(int,input().split())
    print(tree(n1,n2))