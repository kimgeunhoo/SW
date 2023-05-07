'''
2023-05-07
김근호
#문제 정의
3+6+9+...+N 형태로 3의 배수를 더한다
숫자 입력
3의 배수의 총합이 입력된 숫자를 넘었을 때 N 값으 총합계, N값이 몇 번째인지 while 반복문을 사용하는 프로그램 작성
#문제 분석
    변수 : N값(N), 총합 : total
    N을 넘었을 때의 값은
        three + 3 
        N을 넘었을 때, 몇번째 3의 배수인가?
        (three + 3) // 3
#알고리즘
    1.변수 선언
    total = 0
    N = int(input("숫자 입력 : "))
    three = 3
    2.while문을 이용해 3의 배수 연산  
    while (three <= N)
        three += 3
    3. 순차적으로 출력
    print ("N을 넘겼을 때의 값:")
    print ("N을 넘겼을 때까지의 총합:") 
    print ("N을 넘겼을 때까지 몇번째 3의 함수:")
'''
total = 0
three = 3
N = int(input("사용자 입력 : "))
if (N > 3) : # N이 3보다 클때
    if (N % 3 != 0) : # N과 3을 나눈 나머지가 0이 아닐 때.
        while (three < N) : # 3의 배수가 N값이 될 때 까지 
            total += three # N값을 넘긴 총합 계산
            three += 3 # N을 넘긴 값 -3 계산
        if (three < N) : # N을 못 넘기는 경우
            three += 3 
            total += 3 # N을 넘긴 값 계산
        print("{}를 넘겼을 때의 값  : {}".format(N, three))
        print("{}을 넘겼을 때까지의 총합 : {}".format(N, total)) 
        print("{}을 넘겼을 때까지 몇 번째 3의 배수인가 : {}".format(N, three // 3))
elif (N < 3) : # N이 3을 넘기지 못했을 때
    total = 3
    three = 3
    print("{}를 넘겼을 때의 값  : {}".format(N, three))
    print("{}을 넘겼을 때까지의 총합 : {}".format(N, total)) 
    print("{}을 넘겼을 때까지 몇 번째 3의 배수인가 : {}".format(N, three // 3))
