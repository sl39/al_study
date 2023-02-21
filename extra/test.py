import sys
# sys.stdin = open('printer_queue_input.txt')
from collections import deque
input = sys.stdin.readline

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = deque(enumerate(list(map(int, input().split()))))
    priority = list(arr)
    count = 0
    while max(arr, key=lambda x: x[1]) != priority[M]:
        while max(arr, key=lambda x: x[1]) != arr[0]:

                    arr.append(arr.popleft())
        arr.popleft()
        count += 1
    count += 1
    print(count)