'''
2023-05-07
김근호
#문제 정의
    10개의 숫자를 입력받아 0보다 큰 수에 대해서만 전체 합과 평균을 while 이용해 출력하는 프로그램
#문제 분석
    변수: 숫자 10개를 입력받을 반복횟수(count), 10개의 총합(total), 숫자(num), 평균(avg)
#알고리즘
    1. 변수 선언 count, total, num(평균이니 float작성) 
    2. if, while문을 사용해 작성 
    while (count < 10) :
        num = float(input("숫자 입력 : "))
        if (num > 0) :
            total += num
        count += 1;
    if (count > 0) :
        avg = total / count
        print("전체 합 : {}, 평균 : {}".format(total,avg))   
'''
total = 0 # 총합
avg = 0 # 평균
count = 0 # 반복 횟수
while (count < 10) : # 10회 반복
    num = float(input("숫자 입력 : ")) # 평균값을 구해야 하기에 float 작성
    if (num > 0) : # 0보다 큰 숫자일때만 작동  
        total += num # 
    count += 1 # 횟수 카운트
if (count > 0) : # 0이하 숫자를 제외한 평균 계산
    avg = total / count
    print("전체 합 : {}, 평균 : {}".format(total,avg))

   
 
