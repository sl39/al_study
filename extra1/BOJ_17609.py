n = int(input())
arr = []
for i in range(n):
    word = input().strip()
    start = 0
    end = len(word) - 1
    cnt = 0
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            cnt += 1
            if cnt == 2:

                break
            if start == end -1:

                break
            if word[start+1] == word[end]:
                start += 1
                a = word[start:end+1]
                if a == a[::-1]:
                    break
                else:
                    start -= 1
            if word[start] == word[end-1]:
                end -= 1
                a = word[start:end+1]
                if a == a[::-1]:
                    break
                else:
                    cnt = 2
                    break

    print(cnt)
