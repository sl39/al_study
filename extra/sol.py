a = "0269FAC9A0"

res = ""
for i in a:
    res += bin(int(i,16))[2:]

b = len(res)
res = res[2:b-2]
for i in range(len(res)//6):
    print(int(res[i*6:(i+1)*6],2))


