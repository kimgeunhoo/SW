'''
2023-04-04
김근호
표준입력(input())함수 연습
'''

name = input('이름 : ') # 키보드로 이름을 입력받아서 name변수에 문자로 저장
score1 = input('국어 성적 : ') # 국어 성적 score1변수에 문자로 저장
score2 = input('수학 성적 : ') # 수학 성적 score2변수에 문자로 저장
print('{}의 점수 합계는 {}다'.format(name,score1+score2))
print('\n') # 한 줄 띄우기

name1 = input('이름 : ') # 키보드로 이름을 입력받아서 name1변수에 문자로 저장
jumsu1 = int(input('국어 성적 : ')) # 국어 성적 jumsu1변수에 정수로 저장
jumsu2 = int(input('수학 성적 : ')) # 수학 성적 jumsu2변수에 정수로 저장
print('{}의 점수 합계는 {}다'.format(name1,jumsu1+jumsu2))
