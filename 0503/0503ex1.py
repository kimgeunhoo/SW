'''
2023-05-03
김근호
반복문 1~10 출력하기, 1~10 까지의 합계 구하기
'''

sum = 0
#for 반복문
for i in range (1, 11) :
    print(i, end = ' ')
    sum = sum + i

print()

#while 반복문
i = 1 # (반복횟수) 초기화
while i <= 10 : # 반복 조건
    print(i, end=' ') # i 출력
    i = i + 1 # i 1증가

