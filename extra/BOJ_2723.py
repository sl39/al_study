TC = int(input())

fact = [0] *12
fact[0] = 1
for i in range(1,12):
    fact[i] = fact[i-1] * i

def combination(n,r):
    return fact[n]//(fact[r]*fact[n-r])


        
res = [0] * (12)
res[1] = 1
for i in range(2,12):
    t = i
    while t >0:
        res[i] += combination(i,t-1)* res[t-1]
        t -= 1
    res[i] += 2**i - 1


for T in range(TC):
    n = int(input())
    print(res[n])