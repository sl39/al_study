def isprime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    if n == 3:
        return 1

    for i in range(2,int(n**(1/2))+2):
        if n%i == 0:
            return 0

    return 1


dit =  {2: [3,9],
     3: [1,7],
     5: [3,9],
     7: [1,3,9]}

arr = [1,3,7,9]

n = int(input())

def prime(k,depth):
    if depth == n:
        print(k)
        return

    if depth == 1:
        for i in dit[k]:
            prime(k*10 + i, depth+1)

    else:
        for i in range(4):
            if isprime(k*10 + arr[i]):
                prime(k*10 + arr[i], depth + 1)


for i in [2,3,5,7]:
    prime(i, 1)
