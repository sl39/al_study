n = int(input())
arr = list(map(str,input().split()))
chosen = [0] * 10
mx = 0
xs = []
ns = []

mn = int("9"*(n+1))
def perm(depth, res):
    global mn, mx,xs,ns
    if depth == n:
        s = 0

        for i in range(n+1):
            s += res[i] *(10**(n-i))
        if s > mx:
            mx = s
            xs = res[:]
        if s < mn:
            mn = s
            ns = res[:]
        return

    if depth == n:
        return


    for i in range(10):
        if depth == -1:
            chosen[i] = 1
            perm(depth+1, res+[i])
            chosen[i] = 0

        elif not chosen[i]:
            if arr[depth] == "<":
                if res[-1] < i:
                    chosen[i] = 1
                    perm(depth + 1, res + [i])
                    chosen[i] = 0
            elif arr[depth] == ">":
                if res[-1] > i:
                    chosen[i] = 1
                    perm(depth + 1, res + [i])
                    chosen[i] = 0

perm(-1, [])

result_mx = ""
result_mn = ""
for i in xs:
    result_mx += str(i)
for i in ns:
    result_mn += str(i)

print(result_mx)
print(result_mn)


