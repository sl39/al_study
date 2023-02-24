# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo&categoryId=AWXRFInKex8DFAUo&categoryType=CODE&problemTitle=%EC%9B%90%EC%9E%90&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

import sys
sys.stdin = open("sample_input.txt")

TC = int(input())

direction = [[0,1],[0,-1],[-1,0],[1,0]]
for T in range(TC):
    n = int(input())
    atom = []
    for i in range(n):
        arr = list(map(int,input().split()))
        atom.append(arr)
    


