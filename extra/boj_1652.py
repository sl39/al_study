A = int(input())
mat = []
for i in range(A):
    mat.append(input().strip())
cnt1 = 0
cnt2 = 0
for i in range(A):
    stay1 = 0
    stay2 = 0
    for j in range(A):
        if mat[i][j] == ".":
            stay1 += 1
        else:
            if stay1 > 1:
                cnt1 += 1
            stay1 = 0
        if j == A - 1:
            if stay1 > 1:
                cnt1 += 1
            stay1 = 0
        if mat[j][i] == ".":
            stay2 += 1
        else:
            if stay2 > 1:
                cnt2 += 1
            stay2 = 0
        if j == A-1:
            if stay2 > 1:
                cnt2 += 1
            stay2 = 0
    stay1 = 0
    stay2 = 0
print(cnt1 ,cnt2)