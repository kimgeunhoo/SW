'''
2023-05-03
김근호
#문제 정의
    1~입력받은 숫자까지의 합계 구하기
#문제 분석
    변수 : 입력받을 숫자(num), 총합(sum) 반복시킬 횟수(i)
#알고리즘
    1. 변수 선언
        num에 정수 입력
        sum = 0
    2. 논리(반복)
        # 조건 1 for 반복문
        sum = 0
        for num in range(1, num + 1) :
            sum = sum + num 
        sum을 출력

        # 조건 2 while 반복문
        sum = 0 # 함수 초기화
        i = 1
        while i <= num :
            sum = sum + i
            i= i + 1
        sum을 출력
'''

#for 반복
num = (int(input("합계를 구할 숫자 입력: ")))
sum = 0 # 합계
for i in range(1, num + 1) : # 조건 for
        sum = sum + i
print("1부터 {}까지 입력받은 숫자의 합: {}".format(num,sum))

#while 반복
num = (int(input("합계를 구할 숫자 입력: "))) # 조건 while
sum = 0 # 합계 함수 초기화
i = 1 # i 함수 초기화
while i <= num :
        sum = sum + i
        i= i + 1
print("1부터 {}까지 입력받은 숫자의 합: {}".format(num,sum))