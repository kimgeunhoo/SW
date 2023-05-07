'''
2023-05-07
김근호
10개의 정수를 입력받아 합을 구하는 프로그램 while문 작성
단 짝수번째 숫자는 양수를 음수로
홀수 번째 숫자는 음수에서 양수로
#문제 분석
    변수 선언 : 총 합계 (total), 입력 함수(num)
#알고리즘
    while 이용하여 숫자 입력
    while (count < 10) :
        num = int(input("숫자 입력"))
        짝수 번째에는 음수 기호 곱하여 연산
        if (num % 2 == 0) :
            num = num * -1
            total += num
        else 
    count += 1

'''
total = 0 # 총합
count = 0 # 반복 횟수
while (count < 10) : # 10회 반복
    num = int(input("숫자 입력 : ")) #정수 입력
    if (count % 2 == 0) : # 두번째 num 값
        num = num * -1 # num값 에 음수 기호 붙여 구현
        total += num
    else : # 홀수 번째는 그대로 출력
        total += num
    count += 1 # 횟수 카운트
print("전체 합 : {}".format(total)) # 값 출력