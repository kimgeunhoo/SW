'''
2023-05-07
김근호
#문제 정의
    1부터 100까지의 합을 구하여 그림과 같이 출력 되게 while반복문 작성
#문제 분석
    변수 : 1~100까지 증가하는 변수(num), 1부터 100까지의 총합(total), 1-10~1-100까지 반복할 변수(count)
#알고리즘
    출력을 while문으로 작성
    while (count < 10) :
        print("1-", num," : ", total)
    1~100까지 합하는 while 변수
    while (num == 100) :
        total += num
        num += 1 
        count += 1      
'''
num = 1 # 시작 숫자
total = 0 # 총합
count = 0 # 횟수
while (num < 101) : # 100회 덧셈
    total += num # 총합 계산
    num += 1 # 1 증가
    count += 1 # 횟수 카운트
    if (count % 10 == 0) :
        if (count != 100) : # 횟수가 100이 아닐 시, 0000 출력
            print("1-", count," : 0000")
        else : # 횟수가 100일 시, 총합 출력    
            print("1-", count," : ", total)  