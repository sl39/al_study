T = int(input())
mat = []
for i in range(T):
    mat.append(input().split())
count1 = 0
print(mat)

for i in range(5):
    cnt = 0
    for j in range(5):
        if mat[i][j] == ".":
            cnt += 1
        else:
            if cnt >1:
                count1 += 1
                cnt = 0
            else:
                cnt = 0
count2 = 0
for i in range(5):
    cnt = 0
    for j in range(5):
        if mat[j][i] == ".":
            cnt += 1
        else:
            if cnt >1:
                count2 += 1
                cnt = 0
            else:
                cnt = 0
print(count1,count2)