#누울 자리를 찾아라 - NxN 방에서 연속 두 칸 이상 빈칸 세기(가로, 세로)
import sys
input = sys.stdin.readline

N = int(input())

room = [list(map(str,input())) for _ in range(N)]

sleep_row = 0
sleep_column = 0

for i in range(N):
    cnt_row = 0
    cnt_column = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt_row += 1
        else:
            if cnt_row >= 2:
                sleep_row += 1
                cnt_row = 0
            else:
                cnt_row = 0

        if room[j][i] == '.':
            cnt_column += 1
        else:
            if cnt_column >= 2:
                sleep_column += 1
                cnt_column = 0
            else:
                cnt_column = 0

    if cnt_row >= 2:
        sleep_row += 1
    if cnt_column >= 2:
        sleep_column += 1

print(sleep_row, sleep_column)