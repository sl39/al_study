n = int(input())
arr = list(map(int,input().split()))

def binar(start,end,target):
    while start < end:
        mid = (start+end)//2
        if target > lis[mid]:
            start = mid + 1
        else:
            end = mid
    
    return end
lis = [arr[0]]

for i in range(1,n):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        idx = binar(0,len(lis)-1,arr[i])
        lis[idx] = arr[i]
    
print(len(lis))


