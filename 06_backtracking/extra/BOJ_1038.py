n = int(input())

result = []
def com(i,res,depth):
    if i == 10:
        if len(res):
            res.sort(reverse=True)
            result.append(int("".join(map(str,res))))
        return


    com(i+1, res+[i],depth+1)
    com(i+1,res,depth)

com(0,[],0)

result.sort()
try:
    print(result[n])
except:
    print(-1)