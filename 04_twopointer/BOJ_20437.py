### 아이디어
### 각 문자열의 위치에 인덱스를 늘려줌
### 그리고 그 길이만큼 인덱스를 넣어줬다면
### 처음과 끝을 빼주고 + 1 을 해준다
### 그리고 맨 앞을 빼줌


TC = int(input())
for T in range(TC):
    visited = [[] for i in range(26)]
    W = input().strip()
    K = int(input())
    mn = len(W)
    mx = -1
    for i in range(mn):
        # 각각의 위치 인덱스를 넣어줌
        visited[ord(W[i])-97].append(i)

        # 그리고 그 길이가 K와 같다면
        if len(visited[ord(W[i])-97]) == K:

            # 그 문자의 인덱스들의 리스트의 처음과 끝을 빼주고 더하기 1을 해주고 cnt 에 저장
            cnt = visited[ord(W[i])-97][-1] - visited[ord(W[i])-97][0] + 1

            # 그리고 그 cnt의 최대값과 최소값을 찾아줌
            mn = min(mn,cnt)
            mx = max(mx,cnt)

            # 그리고 리스트의 맨 앞을 빼줌
            visited[ord(W[i])-97] = visited[ord(W[i])-97][1:]
    
    
    if mx == -1:
        print(-1)
    else:
        print(mn,mx)
    