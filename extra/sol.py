arr = input().strip()
lenth = len(arr)
result = []
stack = []
bracket = []
bit = []
for i in range(lenth):
    char = arr[i]
    if char == "(":
        stack.append(i)
    elif char == ")":
        A = stack.pop()
        bracket.append([A,i])
    if char in "()":
        bit.append(0)
    else:
        bit.append(1)

br = len(bracket)
def comb(i,res):
    global result, bit
    if i == br:
        if len(res) == br:
            pass
        else:
            for j in res:
                for k in j:
                    bit[k] = 1
            l = ""
            for j in range(lenth):
                if bit[j]:
                    l += arr[j]
            result.append(l)
            for j in res:
                for k in j:
                    bit[k] = 0
        return
    comb(i+1,res+[bracket[i]])
    comb(i+1,res)
comb(0,[])
result.sort()
arr = []

for i in result:
    if i not in arr:
        arr.append(i)

for i in arr:
    print(i)


