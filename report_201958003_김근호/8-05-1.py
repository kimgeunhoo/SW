'''
2023-05-27
김근호
#문제정의
    냉면 가게에서 테이블 별 매출을 저장하는 프로그램
#문제 분석
    변수: 테이블 번호 (table), 냉면 그릇 (bowl), 매출표(list)
#알고리즘
    테이블 번호 입력 1~5, 끝은 0
    입력 후 그릇 수를 입력 
    1. 딕셔너리 생성
        sales = {} 
    2. 파일열기 객체 생성(쓰기)
    3. 파일처리
        3.1 (반복)while True :
                    table = 테이블 번호 입력
                    (선택) if table >= 1 and table <= 5 :
                                ...
                           elif table == 0
                                break
    4.파일 닫기
'''

f = open("c:/data/sales.txt", "w") # 매출을 저장할 변수
sales = {}  # 테이블 번호별 매출을 저장할 딕셔너리

while True: # 무한반복
    table = int(input("테이블 번호를 입력하시오(1~5, 끝:0): ")) # 테이블 번호 입력
    if table >= 1 and table <= 5: # 테이블 번호 범위
        bowl = int(input("그릇 수를 입력하시오: ")) # 몇 그릇인지 쓰기
        if table in sales: 
            sales[table] +=7500*bowl # 이미 있는 테이블 번호인 경우 매출을 누적
        else: 
            sales[table] =7500*bowl # 새로운 테이블 번호인 경우 매출을 초기화
    elif table == 0: # 종료 시
        print("영업이 종료되었습니다. 수고하셨습니다.")
        break # 반복문 종료
for table, sol in sales.items(): # 테이블 번호별 매출을 파일에 쓰기
    f.write(str(table) + "번 테이블 매출: " + str(sol) + "\n")
f.close()
