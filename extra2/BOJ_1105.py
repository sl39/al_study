a,b = map(str,input().split())

def eight(a,b):
    if len(a) < len(b):
        return 0
        

    cnt = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            break
        elif a[i] == b[i] and a[i] == "8":
            cnt += 1
    return cnt

print(eight(a,b))