'''
2023.03.28
김근호
윗변 23 아랫변 34 높이 13 사다리꼴의 넓이
변수: 윗변, 아랫변, 높이, 사다리꼴의 넓이
수식:((윗변 + 아랫변) * 높이) / 2
알고리즘: 변수 선언, 사다리꼴 넓이 구하기, 결과 출력
'''
uplang=23 #윗변
downlang=34 #아랫변
height=13 #높이
area=0 #넓이

area=((uplang + downlang) * height) / 2 #수식

print("윗변", uplang,"cm와 아랫변", downlang,
      "cm와 높이", height ,"cm의 사다리꼴의 넓이는 : ", area) #출력