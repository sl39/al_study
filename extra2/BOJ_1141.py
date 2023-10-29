n= int(input())
arr =[]
for i in range(n):
    arr.append(input())

arr.sort()
cnt = 0
for i in range(n-1):
    if len(arr[i]) <= len(arr[i+1]) and arr[i+1][:len(arr[i])]== arr[i]:
        pass
    else:
        cnt += 1
print(cnt+1)

