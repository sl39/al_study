n,p,q = map(int,input().split())

dic = {0: 1,1: 2}

def func(n):
    if n == 1:
        return 2
    if n == 0:
        return 1
    if n in dic:
        return dic[n]
    dic[n] = func(n//q) + func(n//p)
    return dic[n]

func(n)
print(dic[n])