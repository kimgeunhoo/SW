'''
2023-05-03
김근호
#문제 정의
    입력된 수의 구구단 구하기
#문제 분석
    변수 : 입력할 단(dan), 반복 횟수(i)
#알고리즘
    1. 변수 선언
        dan에 정수입력
        i = 1
    2. 논리 (반복-while)
        while i <= 9 :       
            print('dan * i = ',dan * i)
            i = i + 1
'''
dan = int(input("단 입력: "))
i = 1 # 초기화
print("***", dan, "단 ***")
while i <= 9 : # 반복 조건
    print(dan,'x',i,'=',dan * i)
    i = i + 1 # i 1증가



