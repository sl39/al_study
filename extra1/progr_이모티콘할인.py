cost = 0
plus =0 

def dfs(userCost,depth,arr,users,emoticons,n,m):
    global cost,plus
    if depth == m:
        p = 0
        c = 0
        for i in range(n):
            if users[i][1] < userCost[i]:
                c += users[i][1]
            else:
                p += 1
        if p < plus:
            pass
        elif p == plus:
            cost = max(c,cost)
        else:
            plus = p
            cost = c
        return
        return
    for i in arr:
        for j in range(n):
            if users[j][0] <= 1-i:
                userCost[j] += emoticons[depth] * i
        dfs(userCost,depth+1,arr,users,emoticons,n,m)
        for j in range(n):
            userCost[j] -= emoticons[depth] * i
def solution(users, emoticons):
    global cost,plus
    answer = [0,0]
    n = len(users)
    m = len(emoticons)
    arr = [0.9,0.8,0.7,0.6]
    userCost = [0] * n
    depth = 0
    dfs(userCost,0,arr,users,emoticons,n,m)
    return [plus,cost]