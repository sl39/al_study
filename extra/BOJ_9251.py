a = [0] + list(input().strip())
b = [0] + list(input().strip())


al = len(a)
bl = len(b)

arr = [[0]*al for i in range(bl)]

for i in range(1,bl):
    for j in range(1,al):
        if b[i] == a[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1],arr[i-1][j])


print(arr[bl-1][al-1])