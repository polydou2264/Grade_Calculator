# -*- coding: euc-kr -*-
#이민우10517_내신계산기

def sh(a,b):
    m = b*a/100
    return m

def zp(a,b):
    m = b*a/100
    return m

def zd(a,b):
    m = 100 * (a-20+b) / a
    return max

print("1: 지필 → 원점수, 2: 수행 → 원점수, 3: 수행 세부점수 → 수행 → 원점수, 4: 수행 → 절대 컷, 5: 모든 점수 합산 → 원점수")
switch = int(input("모드를 입력하세요: "))

if switch == 1: #1: 지필 → 원점수
    print("<지필 → 원점수> 모드를 선택하셨습니다.")
    print(" ")

    ts_pc = int(input("중간고사 반영 비율을 입력하세요: "))

    print("지필 점수를 입력해주세요(중간 기말) EX) 90 85")

    test_1, test_2 = input().split()
    test_1 = int(test_1)
    test_2 = int(test_2)
    print(" ")

    print("당신의 지필고사 원점수는 ",zp(test_1, pt_pc) + zp(test_2, pt_pc),"입니다.")

elif switch == 2: #2: 수행 → 원점수
    print("<수행 → 원점수> 모드를 선택하셨습니다.")
    print(" ")
    sh_pc = int(input("수행평가 반영 비율을 입력하세요: "))

    print("수행 점수를 입력해주세요(수행점수 100점 만점으로 계산합니다)")
    sh= input()
    sh = int(sh)
    print(" ")

    print("당신의 수행평가 원점수는", sh(sh, sh_pc), "입니다.")



elif switch == 3: #3: 수행 세부점수 → 수행 → 원점수
    print("<수행 세부점수 → 수행 → 원점수> 모드를 선택하셨습니다.") 
    print(" ")
    
    sh_pc = int(input("수행평가 반영 비율을 입력하세요: "))

    cnt = 0
    n = int(input("입력할 세부점수의 개수를 입력하세요: "))

    print("세부점수를 입력하세요:")

    k=n
    i=0
    while k>0:
        cnt = cnt + int(input())
        k = k - 1
    avg = cnt / n


    print("당신의 수행평가 원점수는", sh(avg, sh_pc), "입니다.")




elif switch == 4: #4: 수행 → 절대 컷
    print("<수행 → 절대 컷> 모드를 선택하셨습니다.") 
    sh_1=[]
    n = int(input("수행평가의 개수를 입력하세요:"))
    print(" ")

    i=0
    cnt = 0
    cnt_ts = 0;
    while n>0:
        print(i+1,"번째 수행점수(원점수X)를 입력하세요:", end='')
        k = int(input())
        print(i+1,"번째 수행 비율을 입력하세요:", end='')
        g = int(input())
        cnt_ts = cnt_ts + g
        cnt = cnt + sh(k,g)
        n = n - 1
        i = i + 1
        print(" ")

    j = 100 - cnt_ts
    
    cnt = cnt_ts - cnt

    print(cnt)

    print("당신의 절대 지필 컷 점수는 ", zd(j ,cnt), "입니다.")

elif switch == 5: #5: 모든 점수 합산 → 원점수
    print("<모든 점수 합산 → 원점수> 모드를 선택하셨습니다.")   


