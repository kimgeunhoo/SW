'''
2023-05-09
김근호
#문제 정의
    입력받은 숫자의 팩토리얼 값 계산하기
#문제 분석
    변수 : 정수(num), 팩토리얼(fac), 임시함수(i)
#알고리즘
    1. 변수 초기화
        num 정수 입력
        fac값 1
    2. 논리 (for 반복문)
    for i in range(num, 0, -1) :
        fac = fac * i

'''
num=int(input("팩토리얼 숫자 입력 : "))
fac=1

for i in range(num, 0, -1) : # 반복 조건
    fac = fac * i # 팩토리얼 계산

print("%d의 팩토리얼 값은 : "%num, fac)