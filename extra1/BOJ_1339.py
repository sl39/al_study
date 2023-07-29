n = int(input())
arr = [0] *100
for i in range(n):
    word = input().strip()
    w_l = len(word)
    for j in range(w_l):
        arr[ord(word[j])] += 10**(w_l-j-1)

arr.sort(reverse=True)
ans = 0
for i in range(10):
    ans += arr[i]*(9-i)

print(ans)