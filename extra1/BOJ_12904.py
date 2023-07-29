S = input().strip()
T = input().strip()
S_len = len(S)
T_len = len(T)

flag = 0
start = 0
end = T_len - 1
while S_len < T_len:
    T_len -= 1
    if flag == 1:
        if T[start] == "B":
            flag = 0
        start += 1
    else:
        if T[end] == "B":
            flag = 1
        end -= 1
if flag == 0:
    if S == T[start:end+1]:
        print(1)
    else:
        print(0)
else:
    if S == T[start:end+1][::-1]:
        print(1)
    else:
        print(0)