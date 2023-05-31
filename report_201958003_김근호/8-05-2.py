'''
2023-05-27
김근호
#문제정의
    'sales.txt'를 읽어 테이블별 매출과 총 매출을 'total_sales'에 출력하는 프로그램
#문제 분석
    변수: 테이블의 총 매출(table_total), 하루 총 매출(today_total)
#알고리즘
    테이블 번호는 1~5번, 테이블의 총 매출을 구하고 하루 총 매출을 구해야함
'''
# 테이블별 매출을 저장할 리스트 초기화
table_sales = [0] * 5  # 테이블은 1부터 5까지 존재

total_sales = 0 # 오늘의 총 매출을 저장할 변수 초기화

with open("c:/data/sales.txt", "r") as f: # 'sales.txt' 파일 읽기
    lines = f.readlines()

for line in lines: # 테이블별 매출 합산
    if "번 테이블 매출" in line:
        table, sales = line.split("번 테이블 매출: ")
        table_sales[int(table) - 1] += int(sales)
        total_sales += int(sales)

with open("c:/data/total_sales.txt", "w") as f: # 'total_sales.txt' 파일에 결과 저장
    for table, sales in enumerate(table_sales, start=1):
        f.write(f"{table}번 테이블 매출: {sales}\n")
    f.write(f"\n오늘의 총 매출: {total_sales}")


for table, sales in enumerate(table_sales, start=1):  # 결과 출력
    print(f"{table}번 테이블 매출: {sales}")
print(f"\n오늘의 총 매출: {total_sales}")




