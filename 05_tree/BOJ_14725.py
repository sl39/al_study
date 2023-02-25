# 블로그 아이디어 차용
# 딕셔러리 안에 딕셔러리를 계속해서 만들어서 함
# trie 를 만들어 볼까 하다가 이건 공부를 더 해봐야 겠다는 생각이 더 들었음
# 함수를 2개를 만드는데 하나는 딕셔러리를 계속해서 넣는것과
# 다른 하나는 print 하는 함수




N = int(input())
mat = []
for i in range(N):
    mat.append(list(input().split()))


# ant 함수를 만듬
def ant(dic,arr):

    # 마지막 까지 해서 할게 없다면 그냥 리턴
    if len(arr) == 0:
        return
    
    # 아니라면 arr[0] 가 없다면 새로 key를 만들고
    if arr[0] not in dic:
        dic[arr[0]] = {}
    
    # 계속해서 잘라서 넣어줌
    ant(dic[arr[0]],arr[1:])


dic = {}

# 밑으로 탐색하면서 하나씩 출력해줌
def pd(dic, depth):
    for i in sorted(dic):
        print("--"*depth,end="")
        print(i)
        pd(dic[i], depth+1)


for i in mat:
    ant(dic,i[1:])

pd(dic,0)

