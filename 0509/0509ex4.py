'''
2023-05-09
김근호
#문제 정의
    1~100까지의 입력받은 숫자의 배수의 합계
#문제 분석
    변수-정수(num), 합계(sum),반복변수(i)
#알고리즘
    1.변수 초기화
        num 변수에 정수를 입력
        sum=0
        i=0
    2.프로그램 논리(반복 안에 선택문-while,if)
        while (i < 100) :
            i = i + 1
            if문 사용(continue)
            if (i % num) != 0
                continue
            sum = sum + i
'''
num=int(input("배수 숫자 입력: "))

i=0
sum=0 # 합계

while (i < 100) : # 반복 조건
    i = i + 1 
    if (i % num) != 0 : # 선택 조건 (i가 num의 배수가 아니면)
        continue # 반복의 처음으로
    sum=sum+i # num의 배수만 더하기

print("1~100까지의 {}의 배수의 합계 : {}".format(num,sum))

