import sys
input = sys.stdin.readline

N = int(input())
# room = [list(input().split()) for _ in range(N)]
room = [list(input()) for _ in range(N)]

sleep_cnt_col = 0
sleep_cnt_row = 0
for i in range(N):
    cnt_col = 0
    cnt_row = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt_col += 1
        else:
            if cnt_col >= 2:
                sleep_cnt_col += 1
                cnt_col = 0
            else:
                cnt_col = 0

        if room[j][i] == '.':
            cnt_row += 1
        else:
            if cnt_row >= 2:
                sleep_cnt_row += 1
                cnt_row = 0
            else:
                cnt_row = 0
        
    if cnt_row >= 2:
        sleep_cnt_row += 1
    if cnt_col >= 2:
        sleep_cnt_col += 1

print(sleep_cnt_col, sleep_cnt_row)