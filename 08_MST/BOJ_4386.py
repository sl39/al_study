# 크루스칼 이용
# 각 별들 사이의 거리와 각각의 별들에게 부여한 임의의 번호를 저장
# 그리고 크루스칼 이용

n = int(input())


arr = [i for i in range(n)]
graph = []
stars = []
for i in range(n):
    stars.append(list(map(float,input().split())))

# 각각의 별들의 거리를 저장하고
# 각각의 별들의 번호와 함께 저장
for i in range(n-1):
    for j in range(i+1,n):
        x,y = stars[i]
        a,b = stars[j]
        dis = ((x-a)**2 + (y-b)**2)**(1/2)
        graph.append((dis,i,j))
    
graph.sort()


# 크루스칼 이용

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]


ans = 0

for i in graph:
    cost , a, b, = i
    aa = find(a)
    bb = find(b)
    if aa != bb:
        if aa > bb:
            arr[aa] =bb
        else:
            arr[bb] = aa
        ans += cost
print(ans)