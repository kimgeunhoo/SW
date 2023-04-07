'''
2023-04-05
김근호
내야하는 총 자동차 세금 구하기(p117-15)
'''

cartax = int(input("자동차 세금 입력: ")) # 자동차 세금 입력
addchg = cartax * 0.03 # 가산세 계산
totalcartax = cartax + addchg # 내야하는 총 자동차 세금 계산

print("자동차 세금이 {}원이고 가산세가 {}원일시 지불해야할 총 자동차 세금은 {}원이다. ".format(cartax,addchg,totalcartax)) # 총 지불해야 할 자동차 세금 출력