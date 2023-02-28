n = int(input())

count = 0
visited = [0] * n
def queen(depth,res):
    global count
    if depth == n:
        count += 1
        return

    if not res:
        for j in range(n):
            if not visited[j]:
                visited[j] = 1
                queen(depth+1,res+[j])
                visited[j] = 0
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
