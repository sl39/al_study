arr = [2,3,5,7,11,13,17]
v = [1] * 19
for i in arr:
    v[i] = 0

n = int(input())/100
m = int(input())/100

fact = [0]*19
fact[0] = 1
for i in range(1,19):
    fact[i] = fact[i-1] * i

ansn = 0
ansm = 0

for i in range(19):
    if v[i]:
        ansn += fact[18] / (fact[i] * fact[18-i]) * (n**i) *((1-n)**(18-i))
        ansm += fact[18] / (fact[i] * fact[18-i]) * (m**i) *((1-m)**(18-i))

print(1-ansn*ansm)