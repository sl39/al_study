## 트리에서 자식노드의 부모노드는 하나밖에 없다
## 그래서 N+1 의 리스트를 생성하고
## mat[자식] = 부모 이다
## 그래서 자식의 조상을 거슬러 올라가는 리스트를 만든다
## 그리고 자신도 다른 노드의 조상이 될 수 있으므로
## 자신을 맨앞에 노드를 삽입하고 시작한다
## 그리고 루트 노드는 부모 노드가 없으니 비어 있을 것이다

TC = int(input())

def tree(n):
    ls = [n]                        # 자신을 넣을 리스트 생성
    while mat[n]:                   # 조상 노드에 도착할 때 까지
        ls.append(mat[n])           # 부모노드들을 아래서부터 순차적으로 추가
        n = mat[n]
    return ls                       # 리스트 반환

for _ in range(TC):
    N = int(input())
    mat = [0] * (N+1)
    for i in range(N-1):
        parents , child = map(int,input().split())
        mat[child] = parents         # child의 위치에다가 부모노드를 저장 
    n1 ,n2 = map(int,input().split())
    t1 = tree(n1)
    t2 = tree(n2)
    for i in t1:                    # 둘이 공통 조상은 반드시 있으므로
        if i in t2:                 # t1 에 하나씩 찾으면서 t2 랑 동일한 거 있는지 확인
            print(i)
            break

    