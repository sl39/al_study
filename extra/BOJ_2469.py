k = int(input())
n = int(input())

alpha = [i for i in range(k)]
pp = list(input().strip())

for i in range(k):
    pp[i] = ord(pp[i]) - 65

mat = []

for i in range(n):
    arr = list(input().strip())
    if arr[0] == '?':
        start = i
    mat.append(arr)
for j in range(start):
    for i in range(k-1):
        if mat[j][i] == '*':
            pass
        else:
            alpha[i], alpha[i+1] = alpha[i+1], alpha[i]

for j in range(n-1,start,-1):
    for i in range(k-1):
        if mat[j][i] == '*':
            pass
        else:
            pp[i], pp[i+1] = pp[i+1], pp[i]

res = ""
for i in range(k-1):
    if alpha[i] == pp[i+1] and alpha[i+1] == pp[i]:
        res += '-'
    else:
        res += '*'

for i in range(k-1):
    if res[i] == "*":
        pass
    else:
        alpha[i],alpha[i+1] =  alpha[i+1],alpha[i]

if alpha == pp:
    print(res)
else:
    print('x'*(k-1))

