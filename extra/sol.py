# from collections import deque


# def BFS(N):
#     queue = deque([])
#     queue.append(N)
#     while queue:
#         x = queue.popleft()
#         if x == K:
#             print(second[x])
#             break
#         else:
#             for nx in ( 2*x,x-1, x+1,):
#                 if 0 <= nx <= 100000 and second[nx] == 0:
#                     if nx == 2*x and visited[nx] ==0: #####
#                         second[nx] = second[x]
#                         visited[nx] = 1               #####
#                         queue.append(nx)
#                     else:                             #####
#                         if visited[nx] == 0:
#                             second[nx] = second[x] + 1 
#                             visited[nx] = 1
#                             queue.append(nx)

# N, K = map(int, input().split())
# second = [0] * 100001
# visited = [0] * 100001                              ########
# BFS(N)



from collections import deque


def BFS(N):
    queue = deque([])
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(second[x])
            break
        else:
            for nx in (x-1, x+1, 2*x):
                if 0 <= nx < 10 and second[nx] == 0:
                    if nx == 2*x:
                        second[nx] = second[x]
                        queue.append(nx)
                    else:
                        second[nx] = second[x] + 1
                        queue.append(nx)

N, K = map(int, input().split())
second = [0] * 10

BFS(N)
print(second)