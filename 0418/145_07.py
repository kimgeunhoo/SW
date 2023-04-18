'''
2023-04-18
김근호
x값 y값을 입력해 x가 크면 나눗셈을, y가 크면 덧셈, x와 y가 같으면 곱셈하기
단, 나눗셈 중에 y값이 0이면 'y값이 0입니다' 출력하기
#문제분석
    변수:x y
    수식:x / y, x + y, x * y
#알고리즘
    1.변수 선언
        x,y에 정수 입력
    2.논리(선택-중첩-if문)
        if (x > y) :
            if (y != 0) :
                print(x // y)
            else :
                print("y 값이 0입니다")
        elif (x < y) :
            print(x + y)
        else :
            print(x * y)

'''

x = int(input("x값 입력: ")) # x 정수로 입력
y = int(input("y값 입력: ")) # y 정수로 입력

if (x > y) : # x가 y보다 클 때
    if (y != 0) : # y가 0이 아닐 때
        print(x // y) # 나눗셈 몫 출력
    else :
        print("y 값이 0입니다") # y값이 0일 때
elif (x < y) : # y가 x보다 클 때
    print(x + y) # 더하기
else : # x y 같은 값일 때
    print(x * y) # 곱하기
 