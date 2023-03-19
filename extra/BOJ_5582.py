a = input().strip()
b = input().strip()

al = len(a)
bl = len(b)

visited = [[0]*al for i in range(bl)]
for j in range(al):
    if a[j] == b[0]:
        visited[0][j] = 1

for i in range(bl):
    if a[0] == b[i]:
        visited[i][0] = 1
for i in range(1,bl):
    for j in range(1,al):
        if a[j] == b[i]:
            visited[i][j] = visited[i-1][j-1] + 1
mx = 0
for i in visited:
    mx = max(mx,max(i))
print(mx)