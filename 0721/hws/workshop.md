# 0721 workshop 최다은

### 1. 간단한 N의 약수

```python
N = int(input())
result = []

for n in range(N):
    if N % (n+1) == 0:
        result.append(n+1)

print(result)
```

### 2. List의 합 구하기

```python
def list_sum(list):
    result = 0
    for element in list:
        result = result + element
    return result
```

### 3. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(list):
    result = 0
    for dic in list:
        result = result + dic['age']

    return result
```

### 4. 2차원 List의 전체 합 구하기

```python
def all_list_sum(LIST):
    result = 0
    for list in LIST:
        for num in list:
            result = result + num

    return result
```

### 5. 숫자의 의미

```python
def get_secret_word(nums):
    result = ''
    for num in nums:
        result = result + chr(num)
    return result
```

### 6. 내 이름은 몇일까

```python
def get_secret_number(chars):
    result = 0
    for char in chars:
        result = result + ord(char)
    return result
```

### 7. 강한 이름

```python
def get_strong_word(word1,word2):
    result1 = 0
    result2 = 0

    for word in word1:
        result1 = result1 + ord(word)
    for word in word2:
        result2 = result2 + ord(word)

    if result1 > result2:
        return word1
    elif result1 < result2:
        word2
    else:
        return word1, word2
```
