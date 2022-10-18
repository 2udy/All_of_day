salt = []
water = []

for i in range(5):
    value = input ('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
    if value == 'Done':
        break
    else: 
        salt.append(value.split('%')[0])
        water.append(value.split('%')[1].strip('g'))

def mass_percent(percent,amount):
    #percent ['4','1','3','5','5']
    #amount ['100','500','200','100','100']
    sum_salt = 0 #전체 소금 양 구하기
    sum_water =0
    for i in range(len(percent)):
        sum_salt += int(amount[i])*int(percent[i])/100
        sum_water += int(amount[i])

    return f'{round(sum_salt/sum_water*100,2)} % {sum_water} g'

print(mass_percent(salt,water))