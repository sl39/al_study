# 소수가 되는 기준만 몇개 생각해봄
# 1자리에선 2 3 5 7
# 2자리수에선 23 29, 31,37 , 53,59, 71,73,79
# 그 다음 부턴 1,3 ,7, 9 각각 넣어보면서 해본다


# 소수인지 판별
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

# 2자리수 일때는 얘네들 가능
dit =  {2: [3,9],
     3: [1,7],
     5: [3,9],
     7: [1,3,9]}

# 아닐때는 얘네들 다 찾아봄
arr = [1,3,7,9]

n = int(input())


#하나씩 해보면서 *10에 + 1,3,5,7 중 하나를 더해봄
def prime(k,depth):
    
    # 그리고 n 자리수 일때 프린트
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
