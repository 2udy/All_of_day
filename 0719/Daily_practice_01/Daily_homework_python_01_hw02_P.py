s = int(input('숫자를 입력해주세요 : '))
rem = 0
sum = 0 

while s != 0:
    rem = s%10
    s = s//10
    
    sum = sum + rem

print(sum)
