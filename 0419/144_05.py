'''
2023-04-19
김근호
두개의 숫자를 입력받아 두 번째 수가 첫 번째 수의 약수인지 구분하기.
#문제분석
    변수-정수1(num1), 정수2(num2)
    수식-num1 % num2 == 0 (num2는 num1의 약수)
#알고리즘
    1.변수 선언
        num1, num2 정수로 입력받기
    2. 논리(선택 if~else)
        if (num1 % num2 == 0) :
            /* num2는 num1의 약수 */
            print("{}는 {}의 약수이다.".format(num2,num1))
        else :
            /* num2는 num1의 약수가 아니다 */
            print("{}는 {}의 약수가 아니다.".format(num2,num1))
'''

num1= int(input("첫 번째 정수를 입력하세요:")) # 첫 번째 정수 입력
num2= int(input("두 번째 정수를 입력하세요:")) # 두 번째 정수 입력

if (num1 % num2 == 0) : # 나머지가 0일 때
    print("{}는 {}의 약수이다.".format(num2,num1)) # 조건 참
else : # 나머지가 0이 아닐 때
    print("{}는 {}의 약수가 아니다.".format(num2,num1)) # 조건 거짓