import sys
input_ = sys.stdin.readline
st = input_().strip()
cnt = 0                                             #P의 갯수를 셀 cnt
l_st  = len(st)                                     #받은 문자열의 길이

if st[l_st-1] == "A":                               #만약에 맨 끝 글자가 A이면 NP를 출력하고 종료
    print("NP")
    quit()

else:
    for i in range(l_st):                           #하나씩 세는데
        if st[i] == "P":                            #일단 i번째가 P이면 cnt+= 1
            cnt+= 1
        else:
            if cnt >=2 and st[i+1]=="P":            #A 이면 앞에 cnt가 2이상이고 i+1 번째가 P 이면
                cnt -= 2                            #cnt -= 2 를 한다
            else:
                print("NP")                         #i+1 번째가 A이면 NP를 출력하고 종료
                quit()

if cnt == 1:                                        #cnt가 1이란 말은 PPAP를 P로 모두 변환 시켜 남은게 P밖에 안남았다는 말이므로 PPAP
    print("PPAP")
else:
    print("NP")                                     #cnt가 1이 아니란 말은 A를 모두 제거 했는데도 P가 2개이상 남았으므로 NP 출력