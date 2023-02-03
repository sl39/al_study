import sys
input = sys.stdin.readline

n, k = map(int, input().split())
student = [0] * n                       # 들어온 순서대로 이름의 길이를 담을 리스트 생성
num = [0] * 21                          # 글자 수 크기가 2~21
count = 0

for i in range(n):                      
    student[i] = len(input().strip())
    if i > k:                           # 하나씩 순회 했을때 k 보다 크다면 
        num[student[i - k - 1]] -= 1    # i가 k 보다 크다면 앞에 지나간건 i-k 번째 있는건 
                                        # 필요 없으므로 하나 지움
    count += num[student[i]]            # 그리고 새로 들어온 이름과 같은 길이는 앞에 있는 길이의 개수만큼
                                        # 더해줌
    num[student[i]] += 1                # 그리고 길이에다가 하나를 더해줌

print(count)