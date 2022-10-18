# 0725 homework 최다은

### 1. 모음은 몇 개나 있을까?

```python
def count_vowels(word):
    vowels = 'aeiou'
    result = 0
    for vowel in vowels:
        result += word.count(vowel)
    return result
```

### 2. 문자열 조작

(4) `.strip([chars])`는 특정문자를 지정하지 않으면 공백 `및 개행 문자`를 제거함

### 3. 정사각형 만들기

```python
def only_square_area(widths,heights):
    square = []
    for width in widths:
        for height in heights:
            if width == height:
                square.append(width**2)
    return square
#comprehension
result = [width*height for width in widths for height in heights if width == height]
```

