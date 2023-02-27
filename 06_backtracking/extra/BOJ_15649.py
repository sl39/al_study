n = int(input())

nums = list(map(int,input().split()))

arr = list(map(int,input().split()))
s = sum(arr)
k = nums[0]
mx = - 1e9
mn = 1e9
def cal(k,depth):
    global mx, mn
    if depth == s:
        if k > mx:
            mx = k
        if k < mn:
            mn = k

    if arr[0]:
        arr[0] -= 1
        cal(k+nums[depth+1],depth+1)
        arr[0] += 1

    if arr[1]:
        arr[1] -= 1
        cal(k-nums[depth+1],depth+1)
        arr[1] += 1

    if arr[2]:
        arr[2] -= 1
        cal(k*nums[depth+1],depth+1)
        arr[2] += 1

    if arr[3]:
        arr[3] -= 1
        if k < 0:
            k = -k
            cal((-1) * (k // nums[depth + 1]), depth + 1)

        else:
            cal(k//nums[depth+1],depth+1)
        arr[3] += 1

cal(k,0)
print(mx)
print(mn)