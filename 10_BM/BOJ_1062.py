n,m = map(int,input().split())

words = []
for i in range(n):
    words.append(set(list(input().strip())))

for i in range(n):
    words[i] = list(words[i])
    k = 0
    for j in words[i]:
        k += 1<<(ord(j)-ord('a'))
    words[i] = k
com = [1<<i for i in range(26)]
base = ['a','c','t','i','n']
for i in range(5):
    base[i] = 1<<(ord(base[i]) - ord('a'))
    com.remove(base[i])
mx = 0


def comb(res,i,depth):
    global mx


    if depth == m-5:
        s = sum(base)
        for j in res:
            s += j
        cnt = 0

        for j in words:
            
            if s&j == j:
                cnt += 1
        mx = max(cnt,mx)
        return
            
    if i == 21:
        return
    
    comb(res+[com[i]],i+1,depth+1)
    comb(res,i+1,depth)

if k< 5:
    print(0)
else:
    comb([],0,0)
    print(mx)