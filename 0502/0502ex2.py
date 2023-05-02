'''
2023-05-02
김근호
range() 함수 - 순차적 범위의 숫자 생성하는 함수
'''
for i in range(10) : # 반복 조건
    print(i, end=' ') # 반복 조건이 참일 동안 반복

print()    

for i in range(1, 10) : # 반복 조건
    print(i, end=' ') # 반복 조건이 참일 동안 반복

print()

for j in range(1, 11, 2) : # 반복 조건
    print(j, end=' ') # 반복 조건이 참일 동안 반복, 홀수 출력

print()

for num in range(10, 0, -1) : # 반복 조건
    print(num, end=' ') # 반복 조건이 참일 동안 반복, 역순 출력