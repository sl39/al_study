N = int(input())
five = N//5
result = 0
res = N - five*5
for i in range(0,five+1):
    if res%3 ==0:
        result = five -i + res//3
        break
    res = res + 5
if result == 0:
    print(-1)
else:
    print(result)