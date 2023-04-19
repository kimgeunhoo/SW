'''
2023-04-19
김근호
입력받은 숫자가 양수, 0, 음수인지 판단
#문제분석
    변수-정수(num)
    수식
        num>0 양수
        num<0 음수
#알고리즘(단순if)
    1. 변수 선언
        num에 정수 입력
    2.논리(선택)
        if num > 0 :
            양수
        if num < 0 :
            음수
        if num == 0 :
            "0"
#알고리즘(다중if)
    1. 변수 선언
        num에 정수 입력
    2.논리(선택)
        if num > 0 :
            양수
        elif num < 0 :
            음수
        else :
            "0"
'''
num = int(input("숫자 입력: "))
# 단순 if
if (num < 0) :
    print("입력값 {}는 음수입니다.".format(num))
if (num > 0) :
    print("입력값 {}는 양수입니다.".format(num))
if (num == 0 ) :
    print("입력값 {}는 0입니다.".format(num))

# 다중 if
if (num < 0) :
    print("입력값 {}는 음수입니다.".format(num))
elif (num > 0) :
    print("입력값 {}는 양수입니다.".format(num))
else :
    print("0입니다.")