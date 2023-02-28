a = "01D06079861D79F99F"
b = ""

for i in a:
    b += bin(int(i,16))[2:]
print(b)
for i in range(len(b)//7):
    print(int(b[i*7:(i+1)*7],2))