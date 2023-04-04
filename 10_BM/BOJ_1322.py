a = list(range(1,5))

for i in range(1<<5):
    arr = []
    for j in range(5):
        if i&(1<<j):
            arr.append(j)
    print(arr)
    