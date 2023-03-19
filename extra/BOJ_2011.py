n = input().strip()

k = len(n)
if "0" == n[0]:
    print(0)
elif k == 0:
    print(0)
elif k == 1:
    print(1)

else:
    arr = [0] * (k+2)
    arr[0] = 1
    for i in range(k-1):
        if n[i] != "0":
            arr[i+1] += arr[i]
            if n[i] == "1":
                arr[i+2] += arr[i]
            elif n[i] == "2":
                if n[i+1] in "0123456":
                    arr[i+2] += arr[i]
            else:
                if n[i+1] == "0":
                    print(0)
                    exit()
    if n[-1] != "0":
        arr[k] += arr[k-1]
    print(arr[k]%1000000)