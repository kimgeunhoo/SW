'''
2023-04-05
김근호
지불할 식사 값 구하기(p116-13)
'''

foodfee = int(input("음식값 입력: ")) # 음식값 입력
addtax = foodfee / 10 # 부가세 계산
foodpay = foodfee + addtax # 총 지불 금액 계산

print("음식값이 {}원이고 부가세가 {}원일시 지불해야할 총 금액은 {}원이다. ".format(foodfee,addtax,foodpay)) # 지불해야 할 음식값 출력
