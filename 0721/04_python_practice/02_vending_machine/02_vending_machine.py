print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.


# 1. 금액 넣기
    # money == 0 까지 금액 입력 반복
    while money != 0:
        if money < 0:
                print('금액은 1원 이상 넣어주세요.')
                break
        elif money > 0:
                budget = budget + money
                print(f'현재 누적 금액은 {budget}원 입니다.')
                break
    # money == 0 이면 금액입력 멈추기
    if money == 0:
        break

# 2. 메뉴 출력

board = zip(menus,costs)
allowed_menu=[]

if budget < 500:
    print(f'{budget}원으로 구매 가능한 메뉴가 없습니다.')
else: 
    print(f'{budget}원으로 구매 가능한 메뉴는 다음과 같습니다.')
    if budget >= 500 :
        allowed_menu.append(menus[0])
        print('1. 콜라 500원')
    if budget >= 700:
        print('2. 사이다 700원')
    if budget >= 1200:
        print('5. 초코우유 1200원')
    if budget >= 2000:
        print('4. 오렌지주스 2000원')
    if budget >= 3600:
        print('6. 아메리카노 3600원')   
    if budget >= 3600:
        print('3. 레모네이드 4500원')

# 3. 메뉴 선택
input('구매하실 메뉴의 번호를 입력하세요. : ')





