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
a_len = len(ab)
b_len = len(bb)
bil_list = [0] * b_len
bil_list[0] = 1
for i in range(1,b_len):
    bil_list[i]= bil_list[i-1] + (2**(i-1))*(i+2)

a_cnt = 0
b_cnt = 0
a_sum = 0
b_sum = 0
for i in range(b_len):
    if i == b_len -1 and bb[i] == "1":
        b_sum += b_cnt
        b_cnt += 1
    elif bb[i] == "1":
        b_sum += bil_list[b_len-i-2] + b_cnt*(2**(b_len-i-1))
        b_cnt += 1


for i in range(a_len):
    if i == a_len -1 and ab[i] == "1":
        a_sum += a_cnt
        a_cnt += 1
    elif ab[i] == "1":
        a_sum += bil_list[a_len-i-2] + a_cnt*(2**(a_len-i-1))
        a_cnt += 1

a_sum += a_cnt
b_sum += b_cnt
print(b_sum - a_sum)