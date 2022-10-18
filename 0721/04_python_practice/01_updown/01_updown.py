import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    while True:
        num = int(input('1이상 10000이하의 숫자를 입력하세요. : '))
    
        if num>10000:
            counts += 1
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해 주세요')
        elif num<0:
            counts += 1
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해 주세요')
        elif num > answer:
            counts += 1
            print('Down!!!')
        elif num < answer:
            counts += 1
            print('Up!!!')
        else:
            counts += 1
            print('Correct!!!',counts,'회 만에 정답을 맞히셨습니다.')
            print('\n')
            break

    retry = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. : ')
    if retry == 'y':
        continue
    elif retry == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
        break
    else:
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
        break
    