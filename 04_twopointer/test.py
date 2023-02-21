TC = int(input())
for T in range(TC):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    idx = []
    mx_idx = 0
    rear = 0
    while  len(idx) < n:
        if arr[mx_idx] < arr[rear]:
            mx_idx = rear
        if rear%n == (mx_idx-1)%n:
            rear = mx_idx
            arr[rear] = 0
            idx.append(rear)
        rear = (rear+1)%n
    for i in range(n):
        if idx[i] == m:
            print(i+1)
            break