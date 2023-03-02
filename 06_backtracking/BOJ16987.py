# 문제 이해가 가장 어려웠던 문제

# 아이디어
# 각각의 내구도랑 무게에다가 값을 넣어주고
# 맨 왼쪽부터 시작하여 하나씩 계란을 쳐준다
# dfs로 탐색 마치 순열 같은 느낌으로다가 해주고
# 마지막 계란을 집었을 때는 쳐주고 종료

n = int(input())

sheild = []
weapon = []

for i in range(n):
    s,w = map(int,input().split())
    sheild.append(s)
    weapon.append(w)

result = 0


def egg(left):
    global result
    if left == n:
        cnt = 0

        # cnt는 sheild 리스트에서 0이하인 값들(즉 계란이 부서진 것들)의 개수를 저장할 cnt
        for i in range(n):
            if sheild[i] <= 0:
                cnt += 1
        
        # result 는 그러한 cnt 중 가장 큰 값
        result = max(result,cnt)
        return

    # 만약에 내구도가 남아 있다면
    if sheild[left] > 0:

        # cnt는 혹시 남은 계란이 더 이상 칠게 없는지 확인

        cnt = 0

        # for 문을 돌리면서 하나씩 집어서 부딫히게 한다
        # 다만 안꺠진 것들만 쳐야 됨
        for k in range(n):
            if sheild[k] > 0 and left != k:
                sheild[left] -= weapon[k]
                sheild[k] -= weapon[left]
                egg(left+1)
                sheild[left] += weapon[k]
                sheild[k] += weapon[left]
                
        # 그리고 부서진 계란의 개수를 구함
            elif sheild[k] <= 0 and left != k:
                cnt += 1

        # 만약 cnt가 n-1, 즉 남아 있는 계란이 하나 밖에 없다면 그대로 감
        if cnt == n-1:
            egg(left + 1)
    # 이번에 선택할 계란이 부서져 있다면 다음 것을 탐색
    else:
        egg(left + 1)
egg(0)
print(result)