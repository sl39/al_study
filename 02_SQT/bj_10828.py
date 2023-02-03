import sys
input = sys.stdin.readline
N = int(input())
result = []
top = 0

for i in range(N):
    M = input().split()
    if len(M) == 2:
        result.append(M[1])
        top += 1
    else:
        if M[0] in "top":
            if top:
                print(result[-1])
            else:
                print(-1)
        elif M[0] == "empty":
            if top:
                print(0)
            else:
                print(1)
        elif M[0] == "size":
            print(top)
        else:
            if not top:
                print(-1)
            else:
                top -= 1
                print(result.pop())
