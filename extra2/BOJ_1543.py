a = input()
b = input()

if len(a) < len(b):
    print(0)
    exit()

cnt = 0
al = len(a)
bl = len(b)
t = 0
while t <al- bl+1:
    if a[t:t+bl] == b:
        cnt += 1
        t += bl
    else:
        t += 1
print(cnt)