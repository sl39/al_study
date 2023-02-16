TC = int(input())
for T in range(TC):
    visited = [[] for i in range(26)]
    W = input().strip()
    K = int(input())
    mn = len(W)
    mx = -1
    for i in range(mn):
        visited[ord(W[i])-97].append(i)
        if len(visited[ord(W[i])-97]) == K:
            cnt = visited[ord(W[i])-97][-1] - visited[ord(W[i])-97][0] + 1
            mn = min(mn,cnt)
            mx = max(mx,cnt)
            visited[ord(W[i])-97] = visited[ord(W[i])-97][1:]
    if mx == -1:
        print(-1)
    else:
        print(mn,mx)
    