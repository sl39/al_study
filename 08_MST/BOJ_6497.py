
def find(x,arr):
    if x != arr[x]:
        arr[x] = find(arr[x],arr)
    return arr[x]


while True:


    m,n = map(int,input().split())
    if m == 0 and n == 0:
        break
    arr = [i for i in range(m+1)]
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))

    graph.sort(key=lambda x : x[2])
    res  = 0
    for i in graph:
        res += i[2]
    ans = 0
    for i in graph:
        a,b,c = i
        aa = find(a,arr)
        bb = find(b,arr)
        if aa != bb:
            if aa > bb:
                arr[aa] = bb
            else:
                arr[bb] = aa
            ans += c
    print(res-ans)