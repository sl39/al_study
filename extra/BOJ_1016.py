n,m = map(int,input().split())

mx = (m+n+1)**(1/2)
prime_lst = [1]*(int(mx)+3)
prime_lst[0] = 0
prime_lst[1] = 0
prime= []
for i in range(2,int(mx)+3):
    if prime_lst[i] == 1:
        prime.append(i)
        t = i*2
        while t < int(mx)+3:
            prime_lst[t] = 0
            t += i

arr = [1]*(m-n+1)
for i in prime:
    t = i**2
    for j in range(m-n+1):
        
        if arr[j] and (j+n)%t ==0:
            arr[j] = 0

print(sum(arr))
