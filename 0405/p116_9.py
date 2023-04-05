'''
2023-04-05
김근호
월급 수령액 구하기(p116-9)
'''

sal=int(input("본급 수령액: ")) # 본급 수령액 입력
allo=int(input("보너스 수당액: ")) # 수당 수령액 입력

total = sal + allo # 총합 계산
tax = total / 5 # 세금 계산, 20%면 1/5, *0.2, *20%
total_sal = total - tax # 총 월급 계산

print("본봉이 {}이고, 수당이 {}이면, 이번 달 월급 실수령액은 {}원 입니다.".format(sal,allo,total_sal)) # 결과 출력