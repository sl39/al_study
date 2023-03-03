A = input().strip()

stack = []
AL = len(A)
def result():
    for i in range(AL):
        if A[i] in "([":
            stack.append(A[i])
        elif A[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                stack.append(2)
            elif stack and type(stack[-1]) == int:
                k = 0
                while stack and type(stack[-1]) == int:
                    k += stack.pop()
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(2*k)
                else:
                    return 0
            else:
                return 0 
        
        elif A[i] == "]":
            if stack and stack[-1] == "[":
                stack.pop()
                stack.append(3)
            elif stack and type(stack[-1]) == int:
                k = 0
                while stack and type(stack[-1]) == int:
                    k += stack.pop()
                if stack and stack[-1] == "[":
                    stack.pop()
                    stack.append(3*k)
                else:
                    return 0
            else:
                return 0 
    if "(" in stack or "[" in stack:
        return 0
    else:
        return sum(stack)
print(result())