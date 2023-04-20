answer = []

tickets = [["ICN", "A"], ["A","ICN"],["ICN", "A"]]


def solution(tickets):
    global answer
    start = "ICN"
    dic = {}
    dic1 = {}
    for i in tickets:
        t = i[0]+i[1]
        if t not in dic1:

            dic1[t] = 1
        else:
            dic1[t] += 1

    
    for i in tickets:
        if i[0] in dic:
            dic[i[0]].append(i[1])
        else:
            dic[i[0]] = [i[1]]
    def dfs(depth,i,res,dic,start,dic1):
        global answer
        if depth == i:
            for i in dic1:
                if dic1[i]:
                    return
            answer.append(res)
        if start in dic:
            for j in dic[start]:
                if (start+j)in dic1 and dic1[start+j]:
                    dic1[start+j] -= 1
                    dfs(depth+1,i,res+[j],dic,j,dic1)
                    dic1[start+j] += 1
    
    dfs(0,len(tickets),['ICN'],dic,'ICN',dic1)
    for i in range(len(answer)):
        answer[i] = tuple(answer[i])
    answer.sort()

    return answer[0]