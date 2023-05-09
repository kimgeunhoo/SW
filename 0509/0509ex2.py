'''
2023-05-09
김근호
#문제 정의
    1~1000까지의 입력받은 숫자의 배수만 더하기
#문제 분석
    변수-정수(num), 합계(total)
#알고리즘
    1.변수 초기화
        num 변수에 정수를 입력
        total=0
    2.프로그램 논리(반복for)
        for i in range(num, 1001, num) :
            sum = sum + i
    
'''
num=int(input("합을 원하는 배수 입력: "))
total=0 # 합계

for i in range (num, 1001, num) : # 반복 조건
    total=total+i

print("1~1000까지의 {}의 배수의 합계 : {}".format(num,total))

