n,m = map(int,input().split())
mat = []
for i in  range(n):
    mat.append(list(map(int,input().split())))

flag = 0 
ans = 0
for i in range(n):
    one = 0
    two = 0
    for j in range(m):
        if j != m- 1:
            if mat[i][j] != 0:
                if flag == mat[i][j]:
                    pass
                else:
                    if flag == 2:
                        one += 1
                    else:
                        two += 1
                    flag = mat[i][j]
            else:
                if flag == 0:
                    pass
                else:
                    ans += 1 + min(one,two)
                    one = 0
                    two = 0
                    flag = 0
        else:
            if flag != 0:
                ans += 1 + min(one,two)
                one = 0
                two = 0
                flag = 0
                
    print(ans)

print(ans)