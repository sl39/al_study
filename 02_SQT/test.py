import sys
from collections import deque
input_ = sys.stdin.readline
TC = int(input_())
for _ in range(TC):
    p = input_().rstrip()
    n = int(input_())
    nx = list(map(int,input_().replace("[","").replace("]","").split(",")))
    print(nx[0])