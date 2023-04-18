'''
2023-04-18
김근호
두개의 숫자를 입력받아 두 번째 수가 첫 번째 수의 약수인지 구별하는 프로그램 작성
#문제분석
    변수:첫번째 정수(num1) 두번째 정수(num2)
    수식:num1 % num2 == 0
#알고리즘
    if (num1 % num2 == 0) :
        print("{}는 {}의 약수이다.".format(num2,num1))
    else :
        print("{}는 {}의 약수가 아니다.".format(num2,num1))
'''

num1= int(input("첫 번째 정수 입력:")) # 첫 번째 정수 입력
num2= int(input("두 번째 정수 입력:")) # 두 번째 정수 입력

if (num1 % num2 == 0) : # 나머지가 0일 때
    print("{}는 {}의 약수이다.".format(num2,num1))
else : # 나머지가 0이 아닐 때
    print("{}는 {}의 약수가 아니다.".format(num2,num1))