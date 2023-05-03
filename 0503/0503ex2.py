'''
2023-05-03
김근호
반복문 1~10 출력하기, 1~10 까지의 합계 구하기
'''

#while 반복문
i = 1 # 반복 횟수 초기화
sum = 0 # 합계
while i <= 10 : # 반복 조건
    sum = sum + i # 합계 저장
    i = i + 1 # i 1증가
print("1~10까지의 합계:{}".format(sum))

#i = 1 for은 i 초기화할 필요가 없다. # 반복 횟수 초기화
sum1 = 0 # sum으로 할, 시 합계 초기화
#for 반복문
for j in range (1, 11) : # 반복 조건
    sum1 = sum1 + j # 합계 구하기
print("1~10까지의 합계:{}".format(sum1))