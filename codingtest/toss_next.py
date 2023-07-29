
def solution(maxSize, actions):
    now = 0
    bacc = -1
    frrr = -1
    recent = []
    back = [0] * len(actions)
    front = [0] * len(actions)
    al = len(actions)
    for i in range(al):
        if actions[i] == "B":
            if bacc >= 0:
                frrr += 1
                front[frrr] = now
                now = back[bacc]
                bacc -= 1
                recent.append(now)
        elif actions[i] == "F":
            if frrr >= 0:
                bacc += 1
                back[bacc] = now
                now = front[frrr]
                frrr -= 1
                recent.append(now)
        else:
            if now != int(actions[i]):
                frrr = -1
                if now:
                    bacc += 1
                    back[bacc] = now
                now = int(actions[i])
                recent.append(now)
    if recent:
        visited = [0] *(max(recent)+1)
    answer = []
    lr = len(recent)
    t = 0
    for i in range(lr-1,-1,-1):
        if visited[recent[i]]:
            pass
        else:
            t += 1
            visited[recent[i]] += 10
            answer.append(str(recent[i]))
            if t == maxSize:
                return answer

    return answer
print(solution(3, ["1", "2", "B", "B", "3"]))