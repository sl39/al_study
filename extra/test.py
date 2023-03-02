# 삭제해야 하는 노드 삭제
def num(n):
    for j in range(t):
        if left[j] == n:
            left[j] = 51
        if right[j] == n:
            right[j] = 51
    return

# 삭제해야 하는 노드의 자식 노드 전체 삭제
def delete(n):
    if left[n] < 51:
        delete(left[n])
    left[n] = 51
    if right[n] < 51:
        delete(right[n])
    right[n] = 51
    for j in range(t):
        if parent[j] == n:
            parent[j] = 51
    return

# 부모가 있고, 자식이 없는 노드 세기
def cnt(n):
    global count
    if left[n] == 51 and right[n] == 51:
        count += 1
    if left[n] < 51:
        cnt(left[n])
    if right[n] < 51:
        cnt(right[n])
    return

t = int(input())
tree = list(map(int, input().split()))
parent = [51] * t
left = [51] * t
right = [51] * t
root = 51
node = int(input())
count = 0

# 만약 노드와 루트가 같으면 0 출력
for i in range(t):
    if tree[i] == -1:
        root = i
    elif tree[i] >= 0:
        if left[tree[i]] == 51:
            left[tree[i]] = i
        else:
            right[tree[i]] = i
    parent[i] = i

if node == root:
    print(0)

else:
    num(node)
    delete(node)

    cnt(root)

    print(count)