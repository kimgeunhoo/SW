'''
2023-05-24
김근호
#문제정의
    score1.txt 파일을 읽어와서 각 학생의 등급을 결정하고
    결과를 report1.txt파일에 저장하기

'''
score = [] # 빈 리스트 변수 생성
f = open("C:/data/score1.txt", "r") # 읽기 객체 생성

for i in range(10) : # 10명의 학생 점수 읽어오기
    score.append(f.readline().split()) # 한 줄씩 읽어서 공백을 기준으로 score 리스트에 추가

for j in range(10) : # 10명의 점수에 대한 등급 계산
    score[j][1] = float(score[j][i]) # 문자열 실수로 계산

    if score[j][1] >= 90 : # 점수 90 이상
        score[j].append("A")
    elif score[j][1] >= 80 : # 점수 90 미만 80이상 
        score[j].append("B")
    elif score[j][1] >= 70 : # 점수 80미만 70이상
        score[j].append("C")
    else : # 점수 70미만
        score[j].append("D")
     
for i in range(10) : # 10명의 등급 화면에 출력
    print("{:<5}{:<5}".format(score[i][0], score[i][2]))

f.close()




