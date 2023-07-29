n,k,p,x = map(int,input().split())

# 비트로 계산
# 위에서 부터 차례로 켜져있는곳을 1 꺼져 있는곳을 0이라 한다면
#  0 = '1110111' , 1= '0010010' ,...
# bit = ['1110111', '0010010','1011101', '1011011','0111010','1101011','1101111','1010010','1111111','1111011']
# arr = [[0]*10 for _ in range(10)]

# for i in range(10):
#     for j in range(10):
#         cnt = 0
#         for k in range(7):
#             if bit[i][k] != bit[j][k]:
#                 cnt += 1
#         arr[i][j] = cnt

arr = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

start = '0'*(k-len(str(x))) + str(x) # start = 05

n = '0'*(k-len(str(n))) + str(n)
ans = -1

def backtracking(now,depth,cnt):
    global ans

    # 만약에 어떤 값이 최대층 보다 클때는 return
    if depth and int(now) > int(n[:depth]):
        return
    
    # 깊이가 k 일때
    if depth == k:

        # now 값이 '00000'일때 제외 
        if now=='0'*k:
            return
        
        # cnt가 p보다 작거나 같을 때 ans += 1
        if cnt <= p:
            ans += 1
        return
    
    # cnt > p 보다 크면 return
    if cnt > p:
        return 


    a = int(start[depth])
    for i in range(10):
        backtracking(now+str(i),depth+1,cnt+arr[a][i])
backtracking('',0,0)
print(ans)
