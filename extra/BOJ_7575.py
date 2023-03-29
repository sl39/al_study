n, k = map(int,input().split())

mat = []
code = []
for i in range(n):
    code.append(int(input()))
    a = list(map(int,input().split()))
    mat.append(a)

cl = []
for i in range(code[0]):
    t = 0
    num = code[0][i]
    