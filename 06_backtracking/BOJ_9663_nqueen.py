# 아이디어
# 위에서 부터 하나씩 선택한다

n = int(input())

count = 0
visited = [0] * n

# 퀸을 찾는 과정 depth는 행의 idx
def queen(depth,res):
    global count
    if depth == n:
        count += 1
        return

    # 비어있으면
    if not res:
        for j in range(n):

            # j 비어있으면 넣음
            if not visited[j]:
                visited[j] = 1
                queen(depth+1,res+[j])
                visited[j] = 0
    
    # 세로도 visted에 포함됨
    # 대각선은 이전 인덱스와 이제 행의 값의 절대값이랑 이전 값과 이번에 넣을 값의 차의 절대값이 달라야 됨
    else:
        for j in range(n):
            if not visited[j]:
                point = 0
                for k in range(depth):
                    if abs(res[k]-j) == abs(k-depth):
                        point = 1
                        break
                if not point:
                    visited[j] = 1
                    queen(depth + 1, res + [j])
                    visited[j] = 0



queen(0,[])
print(count)
