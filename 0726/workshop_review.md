# 0726 workshop 최다은

### 1.  무엇이 중복일까

```python
def duplicated_letters(letters):
    result = []
    for letter in letters:
        if letters.count(letter)>1:
            if letter not in result:
                result.append(letter)
    return result

# 교수님
def duplicated_letters(word):
    result = []
    for char in word:
        if word.count(char)>1 and char not in result:
            result.append(char)
    return result
```

### 2. 소대소대

```python
def low_and_up(letters):
    result = ''

    for i in range(len(letters)):
        if i%2 != 0:
            result += letters[i].upper()
        else:
            result += letters[i].lower()
    return result

# 교수님 1
def low_and_up(word):
    result = ''
    for idx,char in enumerate(word):
        if idx %2 == 1:
            result += char.upper()
        else:
            result += char.lower()
    return result
```

### 3. 솔로 천국 만들기

```python
# 첫번째 값을 지정해서 넣는 방법
def lonely(numbers):
    result = [numbers[0]]          
    for number in numbers:
        if number != result[-1]:
            result.append(number)
    return result

# 교수님 1 (조건을 통해서 첫번째 값을 넣는 방법)
def lonely(numbers):
    result = []
    for idx,number in enumerate(numbers):
        if idx == 0 :
            result.append(number)
        if result[-1] != number :
            result.append(number)
    return result
```