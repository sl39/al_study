result = []

def com(res,i,depth):
    global result
    if depth == l:
        vowel = 0
        con = 0
        for i in res:
            if i in "aeiou":
                vowel += 1
            else:
                con += 1
        if vowel >= 1 and con >= 2:
            result.append("".join(res))
        return

    if i == c:
        return
    com(res+[arr[i]], i+1,depth+1)
    com(res,i+1,depth)







l, c = map(int, input().split())
arr = list(map(str,input().split()))
arr.sort()
com([],0,0)

for i in result:
    print(i)
