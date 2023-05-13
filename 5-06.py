'''
2023-05-09
김근호
#문제 정의
사용자로부터 숫자를 하나 입력받아 1부터 입력받은 숫자 사이의 소수를 출력하는 프로그램 작성
#문제 분석
    변수 - 입력값(num), 중복 숫자 제거(delate)
#알고리즘
    입력값에서 1은 제외, 1보다 커야한다
    입력받은 숫자 안에서 소수를 구하려면 반복 2회 시행
    num = int(input("숫자를 입력하세요: "))
    del = []

    for n in range(2, num+1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)

    print(prime_numbers)
'''
num = int(input("숫자를 입력하세요: "))
delate = [] # 중복 제거

for n in range(2, num+1):
    isnum = True
    for i in range(2, n):
        if n % i == 0:
            isnum = False
            break
    if isnum:
        delate.append(n)

print(delate)