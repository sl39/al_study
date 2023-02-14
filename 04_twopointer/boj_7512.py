num = 10000001

plist = [1] * num
plist[0] = 0
plist[1] = 0
prime = []
for i in range(num):
    if plist[i]:
        prime.append(i)
        for j in range(2*i,num,i):
            plist[j] = 0
