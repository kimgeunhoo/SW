'''
2023-04-20
김근호
8세 이상 키 120cm이상인 어린이는 '고속 롤러코스터 입장 가능'
8세 이상 키 120cm미만인 어린이는 '저속 롤러코스터 입장 가능'
8세 미만 어린이는 '입장 할 수 없습니다'를 출력하는 프로그램 작성
#문제 분석
    변수-나이(age), 키(cm)
    수식-8 <= age and cm >= 120
         8 <= age and cm < 120
         8 > age
#알고리즘
    논리(if~elif 다중 if문)
    
    if (8 <= age and cm >= 120) 고속 롤러코스터
    elif (8 <= age and cm < 120) 저속 롤러코스터
    else 탑승 불가
    위도 정답이 되나 뭔가 깔끔해 보이지 않음

    if (8 <= age)
        if (cm >= 120) 고속 롤러코스터
        else 저속 롤러코스터
    else 탑승 불가
'''
age = int(input("나이 입력 : "))
cm = float(input("키 입력 : "))

# if (8 <= age and cm >= 120) : 
#     print("고속 롤러코스터 탑승 가능")
# elif (8 <= age and cm < 120) :
#     print("저속 롤러코스터 탑승 가능")
# else :
#     print("입장 할 수 없습니다.")

if (8 <= age) : 
    if (cm >= 120.0) :
        print("고속 롤러코스터 탑승 가능")
    else :
        print("저속 롤러코스터 탑승 가능")
else : 
    print("입장 할 수 없습니다.")
