'''
2023-04-12
김근호
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수 선언
        num1,num2에 정수 입력
    2.논리(선택)
    if num1 > num2 :
        큰 수는 num1 작은 수는 num2
    elif num1 < num2 :
        큰 수는 num2 작은 수는 num1
    elif num1 == num2 :
        두 수는 같은 숫자이다.
    else :
        정수가 아닌 수를 입력.
'''

num1 = int(input("첫 번째 숫자 입력 : ")); # 첫번째 정수 입력
num2 = int(input("두 번째 숫자 입력 : ")); # 두번째 정수 입력

# if num1 > num2 : 
#     print("두 수 중에 가장 큰 수는 {}이고, 가장 작은 수는 {}이다.".format(num1,num2));
# elif num1 < num2 : 
#     print("두 수 중에 가장 큰 수는 {}이고, 가장 작은 수는 {}이다.".format(num2,num1));
# elif num1 == num2 :
#     print("두 수{},{}는 같은 숫자이다.".format(num2,num1));
# else :
#     print("입력한 숫자는 정수가 아닙니다.");
if num1 > num2 : # 조건
    print("두 수 중에 큰 수는 {}이고, 작은 수는 {}이다.".format(num1,num2)); # 참일때 결과 출력
else :
    print("두 수 중에 큰 수는 {}이고, 작은 수는 {}이다.".format(num2,num1)); # 거짓일때 결과 출력