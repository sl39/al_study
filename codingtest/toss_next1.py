def solution(s, N):
    sl = len(s)
    visited = [0]*(N+1)
    if N == 1:
        mx = 0
        for i in s:
            if mx< int(i) <= N:
                mx = int(i)
        return mx

    for i in range(sl):
        if int(s[i]) <= N:
            end = i
            start = i
            break

    value = 0
    while end < sl:
        if int(s[end]) > N:

            for i in range(end+1,sl):
                if int(s[i]) <= N:
                    end = i
                    start = i
                    break
            continue
        if visited[int(s[end])]:
            while s[end] != s[start]:
                visited[start] -= 1
                start += 1
            start += 1
        else:
            visited[int(s[end])] += 1

        if end - start == N-1:
            if value < int(s[start:end+1]):
                value = int(s[start:end+1])
        end += 1
    return int(value)

print(solution("1451232125", 2))