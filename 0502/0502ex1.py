'''
2023-05-02
김근호
파이썬 내장함수
'''

# 자료형 변환 함수
s = '123144' # s 변수에 문자열 '123'저장

ch1 = int(s) # ch1 변수에 s를 정수로 변환해서 저장
ch2 = list(s) # ch2 변수에 s를 list로 변환해서 저장
ch3 = tuple(s) # ch3 변수에 s를 tuple로 변환해서 저장
ch4 = set(s) # ch4 변수에 s를 집합(set(중복제거))으로 변환해서 저장

print('{}의 자료형은 {}'.format(ch1,type(ch1)))
print('{}의 자료형은 {}'.format(ch2,type(ch2)))
print('{}의 자료형은 {}'.format(ch3,type(ch3)))
print('{}의 자료형은 {}'.format(ch4,type(ch4)))

print() # 한 줄 띄우기

num1 = abs(-5) # num1 변수에 -5의 절대값 저장
num2 = round(4.6) # num2 변수에 반올림값을 저장
num3 = bin(10) # num3 변수에 정수 10을 이진수로 변환해서 저장
str1 = chr(97) # str1 변수에 97에 해당하는 문자를 반환
str2 = ord('A') # str2 변수에 'A'의 아스키 코드값 저장

print('-5의 절대값:', num1)
print('4.6의 반올림값:', num2)
print('정수 10의 이진수 값:', num3)
print('97에 해당하는 문자:', str1)
print('A의 아스키코드 값:',str2)

print() # 한 줄 띄우기

num10=[6, 3, 5, 1, 9, 2, 8] # 리스트 자료형
print('num10 원소의 길이: ', len(num10))
print('num10 원소 중 가장 큰 값: ', max(num10))
print('num10 원소 중 가장 작은 값: ', min(num10))
print('num10 원소들의 합계: ', sum(num10))
print('num10 원소들 정렬: ', sorted(num10)) # 오름차순

print() # 한 줄 띄우기

print(zip('123', ('kim', 'lee', 'part')))

# 문자열과 투플을 묶어서 리스트 자료형으로 반환
print(list(zip('123', ('kim', 'lee', 'part'))))

# 문자열과 투플을 묶어서 투플 자료형으로 반환
print(tuple(zip('123', ('kim', 'lee', 'part'))))


