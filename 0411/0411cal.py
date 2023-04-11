'''
2023-04-11
김근호
선택문-if,if~elif~else
'''
num1=int(input("1번째 정수 입력:"));
op=input("연산자 입력:");
num2=int(input("2번째 정수 입력:"));
if op == "+" :
    print(num1+num2);
elif op == "-" :
    print(num1-num2);
elif op == "*" :
    print(num1*num2);
elif op == "/" :
    print(num1/num2);
else :
    print("유효한 연산자가 아닙니다.")