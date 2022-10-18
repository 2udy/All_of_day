# 0725 workshop 최다은

### 1. 평균 점수 구하기

```python
dic.values

```

### 2. 혈액형 분류하기

```python
def count_blood(bloodtypes):
    result = {
        'A':bloodtypes.count('A'),
        'B':bloodtypes.count('B'),
        'O':bloodtypes.count('O'),
        'AB':bloodtypes.count('AB')
    }
    return result
# 교수님 풀이 1
def count_blood(blood_types):
    result = {}
    
    for blood in blood_types:
        # 키가 있을 때
        if result.get(blood):
            result[blood] += 1
        else:
            result[blood] = 1
    return result

# 교수님 풀이 2
def count_blood(blood_types):
    result = {}
    for blood in blood_types:
        result[blood] = result.get(blood,0) + 1
    return result
```
