'''
2023-05-09
김근호
#문제 정의
    사용자로부터 월을 입력받아 그 월에 해당하는 계절 출력하는 프로그램 작성
#문제 분석
    변수 - 월(month)
#알고리즘
    month가 0이 입력될 때 까지 무한반복 
    반복문 안에 입력값 작성
    3~5월은 봄, 6~8은 여름, 9~11은 가을, 12, 1, 2월은 겨울 출력
    while (True) :
        month = int(input("가장 좋아하는 월은?(종료:0) : "))
        if (3 <= month <= 5) :
            print("{}월은 봄에 해당됩니다".format(month))
        elif (6 <= month <= 8) :
            print("{}월은 여름에 해당됩니다".format(month))
        elif (9 <= month <= 11) :
            print("{}월은 가을에 해당됩니다".format(month))
        elif (12 == month and 1 == month and 2 == month) :
            print("{}월은 겨울에 해당됩니다".format(month))
        elif (month == 0) :
            print("종료")
            break;
'''

while (True) : # 무한루프
    month = int(input("가장 좋아하는 월은?(종료:0) : "))
    if (month == 0) : # 0 입력 시 반복 종료
            print("종료")
            break
    elif (3 <= month <= 5) : # 봄
            print("{}월은 봄에 해당됩니다".format(month))
    elif (6 <= month <= 8) : # 여름
            print("{}월은 여름에 해당됩니다".format(month))
    elif (9 <= month <= 11) : # 가을
            print("{}월은 가을에 해당됩니다".format(month))
    elif (month == 12, 1, 2) : # 겨울
            print("{}월은 겨울에 해당됩니다".format(month))
    



