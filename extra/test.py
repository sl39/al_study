'''
구현 방법 아이디어
1. 입력 값을 첫번째 값으로 설정하고 다음 수를 반복문을 돌려 완전탐색
2. 결과 리스트를 만들어 음수가 나오기 전까지 append
    2-1. 세번째 값부터는 변수를 재할당
        ( 세번째부터 : next = first - second )
        ( first -> second / second -> next )
'''

N = int(input())
num_lst = []

# 첫번째 수가 1이 되는 것을 피하고자 범위 설정
for i in range(N,0,-1):
    second = i
    first = N
    tmp = [first, second]

    while True:
        next = first - second
        if next >= 0:
            tmp.append(next)
            first = second
            second = next
        else:
            if len(tmp) > len(num_lst):
                num_lst = tmp
            break

print(len(num_lst))
print(*num_lst)