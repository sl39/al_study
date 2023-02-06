# 일단 받아들인 표기식을 영어글자, [+,-], [*,/] , ( , ) 이렇게 총 5개로 나누어야 한다
# 영어 글자는 나오게 되면 stack에 넣지 않고 결과 리스트에 집어 넣는다

# * , / 을 스택에 넣고
# 그  다음에 문자가 나오고 그 다음에 ( 가 나오지 않으면 스택에서 pop 한다

# 여기서 더하기와 뺄셈은 무조건 맨 마지막이므로 앞선 모든 계산이 끝날때까지 채워넣는다

# 가장 중요한건 "(" 와 ")"

# "(" 얘는 먼저 스택에 집어넣고
# ")" 나올때까지 기다린다. ")" 가 나오면 "(" 나올때까지 모두 소모



sik = input().strip()
f = ["+","-","*","/"]
f0 = ["+","-","*","/","(",")"]
f1 = ["+","-"]
f2 = ["*","/"]

stack = []
result = []

if sik[0] == "(":
    stack.append(sik[0])

else:
    result.append(sik[0])
ls = len(sik)

for i in range(1,ls):

    if sik[i] not in f0:                    #그냥 문자가 나오면 result에 넣고
        result.append(sik[i])
        if sik[i-1] in f2:                  #문자 이전에 *, / 이면 꺼내서 result에 넣는다
            result.append(stack.pop())

    elif sik[i] in f2:                      # * 와 / 는 그냥 스택에 넣는다
        stack.append(sik[i])

    elif sik[i] in f1:                      # +, - 일 경우는 스택 맨 위에 있는것이 사칙 연산일 경우
        if stack:
            if stack[-1] in f:              #  스택 맨 위에 있는 것을 result에 저장
                result.append(stack.pop())
        stack.append(sik[i])                # 그리고 다시 스택에 저장

    elif sik[i] == "(":                     # ( 은 그냥 저장하고
        stack.append("(")

    else:                                           # )  이 나왔을 경우
        if stack:
            while stack and stack[-1] != "(":           # 스택에서 ( 이 나올때까지 pop 하여 result에 저장
                result.append(stack.pop())
            stack.pop()                                 # 그리고 ( 는 필요 없으니깐 그냥 제거
            if stack:
                if stack[-1] in f2:                     # 그리고 만약에 D+ A*(B+C) 와 D*A + (B+C) 는 경우가 다른데 
                                                        # 이 if 문은 전자의 예외를 해결하기 위해 만듬
                    result.append(stack.pop())

                                                # 그리고 마지막이 됐을 땐 모든 걸 다 저장해야 되므로
while stack:                                    # 스택에 남은걸 다 꺼내서 result에 저장
    result.append(stack.pop())

print("".join(result))
    


