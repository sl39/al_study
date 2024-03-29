# 아이디어
# 일단 각노드들을 연결하는 트리를 만들고
# 주어진 노드의 조상을 찾는다
# 시간 초과를 해결하기 위해서
# 노드의 조상을 찾게되면 새로운 arr 에 그 조상 리스트를 저장한다
# 그리고 노드의 조상들을 뒤에서 같이 하나씩 비교해가며
# 제일 가까운것을 찾느다


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

# 트리를 구성
q = deque([1])
while q:
    node = q.popleft()
    for i in mat[node]:
        if not arr[i]:
            arr[i] = node
            q.append(i)


# 각 노드의 조상을 찾고
# 공통 조상을 찾아나가는 과정
def tree(n1,n2):
    global plist
    if plist[n1]:
        parents1 = plist[n1]
    else:
        parents1 = [n1]
        a = n1
        while a != 1:
            a = arr[a]
            parents1.append(a)
        plist[n1] = parents1
       
    if plist[n2]:
        parents2 = plist[n2]
    else:
        parents2 = [n2]
        b = n2
        while b != 1:
            b = arr[b]
            parents2.append(b)
        plist[n2] = parents2
        

    cnt = 1

    while cnt < min(len(parents1), len(parents2))+1 and parents2[-cnt] == parents1[-cnt]:
        cnt += 1


    return parents1[-cnt+1]


m = int(input())
for i in range(m):
    n1,n2 = map(int,input().split())
    print(tree(n1,n2))
