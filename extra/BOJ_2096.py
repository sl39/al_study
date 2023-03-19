n = int(input())

for i in range(n):
    ls = list(map(int,input().split()))

    if i == 0:

        mxdp = ls[:]
        mydp = ls[:]
        continue
    mx = mxdp[:]
    my = mydp[:]
    for j in range(3):
        if j == 0:
            mxdp[j] = ls[j] + max(mx[0],mx[1]) 
            mydp[j] = ls[j] + min(my[0],my[1]) 
        elif j == 1:
            mxdp[j] = ls[j] + max(mx) 
            mydp[j] = ls[j] + min(my)
        else:
            mxdp[j] = ls[j] + max(mx[2],mx[1]) 
            mydp[j] = ls[j] + min(my[2],my[1])
        
print(max(mxdp),end=" ")
print(min(mydp))