'''
2023-04-05
김근호
5과목 점수 입력 받아서 합계 평균 구하기(p117-14)
'''

sub1 = int(input("과목1:")) #과목1 점수 입력
sub2 = int(input("과목2:")) #과목2 점수 입력
sub3 = int(input("과목3:")) #과목3 점수 입력
sub4 = int(input("과목4:")) #과목4 점수 입력
sub5 = int(input("과목5:")) #과목5 점수 입력

total = sub1 + sub2 + sub3 + sub4 + sub5 # 합계 구하기
avg = total / 5 # 평균 구하기

print("5과목의 합계는 {}아고, 평균은 {}이다.".format(total, avg)) # 출력