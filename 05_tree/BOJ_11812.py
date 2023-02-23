# 아이디어
# k진 트리인데 순서대로 완전히 채워져 있으므로
# 부모 노드를 계속해서 생각한다
# 만약에 두 노드의 크기를 비교했을때
# 크기가 큰 노드의 부모로 바꿔서 비교하고
# cnt += 1
# 계속해서 왔다갔다 하다가 부모가 동일해지면
# cnt를 리턴
# 부모노드가 왜 저렇게 나오는지 알고 싶다면
# 맨 아래 쪽 ㄱㄱ


import sys
input = sys.stdin.readline

def find(x,y):
    cnt = 0

    # 부모노드가 같아질때까지 반복
    while x!=y:
        if x>y:

            # x 번째의 부모 노드는 (x+k-2)//k 이거이다
            x=(x+k-2)//k
            cnt += 1
        else:
            y=(y+k-2)//k
            cnt += 1
    return cnt

n,k,q =map(int,input().split())
for i in range(q):
    x,y = map(int,input().split())

    # 이거 구선생님 빡셉니다
    if k == 1:
        print(abs(x-y))
    
    else:
        print(find(x,y))


# 루트 노드의 레벨을 1이라고 한다면
# l 번째 레벨의 노드 개수는 k**(l-1) 이다
# l 번째 레벨의 노드 중에 c 번째 노드의 부모 p 를 찾아야 한다
# p 번째 노드의 자식들을 알고싶다
# p의 인덱스 값은 1 + k + k^2 + ... + k^(l-2) + p
# 자식들의 인덱스 값은 1 + k + k^2 + ... + k^(l-2) + k^(l-1) + k*(p-1) + 1 부터 + k
# 1 + k + k^2 + ... + k^(l-2) + k^(l-1) + k*(p-1) + 1 부터
# 1 + k + k^2 + ... + k^(l-2) + k^(l-1) + k*(p-1) + k 까지

# p 인덱스를 k 곱하면 k + k^2 + .. k^(l-1) + p*k
# 차이는 -k+2 부터 1까지
# 그래서 각 자식 노드에 k-2 를 더하면 
# 0 부터 k-1 까지이다
# 즉 거꾸로 생각해서 각 자식 노드에 k-2 를 더해서 k로 나누면
# p의 번째 노드를 몫으로 가지고 0~k-1 가 나머지가 된다