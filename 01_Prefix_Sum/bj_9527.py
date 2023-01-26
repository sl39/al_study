A,B = map(int,input().split())


def binar(n):
    if n<2:
        return str(n)
    return binar(n//2) + str(n%2)
ab = binar(A-1)
bb = binar(B)
# bc = bb 까지의 1의 개수합
# ac = ab-1 까지의 1의 개수합
#bc -ac
ac = 0
bc = 0
cnt = 0
while len(bb):
    if bb[0] == '1':
        cnt +=1
        bc += 2**(len(bb)-1) *cnt
        bb = bb[1:]
    else:
        bb = bb[1:]
cnt = 0
while len(ab):
    if ab[0] == '1':
        cnt +=1
        ac += 2**(len(ab)-1) *cnt
        ab = ab[1:]
    else:
        ab = ab[1:]
print(bc-ac)