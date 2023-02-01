import sys
input_ =sys.stdin.readline
N = int(input_())
ls = list(map(int,input_().split()))

r = [-1] *N             #오큰수를 담을 리스트 생성, 디폴트는 -1

stack = [0]             #스택을 넣을 리스트 생성

for i in range(1,N):
    while stack and ls[i] > ls[stack[-1]]:          #스택이 비어있지 않고 i번째보다 스택 맨 위에 있는 수가 작을 경우
        r[stack.pop()] = ls[i]                      #오큰수를 발견 했기 때문에 맨위에 있는 스택을 빼주고, 오큰수를 r 에 저장
    stack.append(i)                                 #아니면 그냥 스택을 쌓음
print(*r)
