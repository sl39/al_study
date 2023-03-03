from itertools import permutations
n = int(input())


for i in range(n):
    arr = list(input().strip())
    arr = tuple(arr)

    mat=(sorted(list(permutations(arr,len(arr)))))

    idx = 0
    while idx < len(mat) and  mat[idx] != arr:
        idx += 1

    while idx < len(mat) and mat[idx] == arr:
        idx += 1
    
    if idx == len(mat):
        print("".join(arr))
    else:
        print("".join(mat[idx]))


