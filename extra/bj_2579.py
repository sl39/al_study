N = int(input())
ls = [0]
for i in range(N):
    ls.append(int(input()))

if N == 1:
    print(ls[1])
elif N == 2:
    print(ls[1]+ls[2])
else:
    l1 = [0]
    l1.append([ls[1],ls[1]])
    l1.append([ls[1]+ls[2],ls[2]])

    for i in range(3,N+1):
        l1.append([l1[i-1][1]+ls[i],max(l1[i-2][0]+ls[i],l1[i-2][1]+ls[i])])
        
    print(max(l1[N]))
    print(l1)