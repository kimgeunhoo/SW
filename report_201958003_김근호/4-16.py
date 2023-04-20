'''
2023-04-20
김근호
직급과 나이를 입력받아 직급이 7 아니면 8, 나이가 40대면 '연금 80%대상자입니다' 를 출력
직급이 5 아니면 6, 나이가 50대면 '연금 10%대상자입니다' 를 출력
#문제분석
    변수:직급(grade) 나이(age) 
    수식: 연금 80% 대상자
        grade == 7 or 8
        40 <= age <= 49 
          연금 100% 대상자
        grade == 7 or 8
        50 <= age <= 59 
#알고리즘
    논리 (if~elif~else 다중 if문)
    if ((grade == 7 or grade == 8) and (40 <= age and age <= 49))
    elif ((grade == 5 or grade == 6) and (50 <= age and age <= 59))
    else 연금 대상자가 아닙니다 출력
'''
grade = int(input("직급 입력 : "))
age = int(input("나이 입력 : "))

if ((grade == 7 or grade == 8) and (40 <= age and age <= 49)) :
    print("연금 80% 대상자입니다.")
elif ((grade == 5 or grade == 6) and (50 <= age and age <= 59)) :
    print("연금 100% 대상자입니다.")
else :
    print("연금 대상자가 아닙니다.")
