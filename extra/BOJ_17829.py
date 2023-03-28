import sys
input = sys.stdin.readline

def pulling(n, x, y, arr, result):

    if n == 2:
        ans = []
        for i in range(y, y + n):
            for j in range(x, x + n):
                ans.append(arr[i][j])
        ans.sort()
        result[y//2][x//2] = ans[2]
        # print(result)
        return
        # return result
    else:

        pulling(n//2, x, y, arr, result)
        pulling(n//2, x+n//2, y, arr, result)
        pulling(n//2, x, y+n//2, arr, result)
        pulling(n//2, x+n//2, y+n//2, arr, result)

    return result

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

while N>2:
    data = pulling(N, 0, 0, data, [[0]*(N//2) for _ in range(N//2)])
    N = N//2
ls = []
for i in data:
    ls = ls + i
ls.sort(reverse=True)
print(ls[1])
