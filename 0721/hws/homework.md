# 0721 homework 최다은

### 1. 위치 인자와 키워드 인자

```python
# (4)
ssafy(name='승호', '광주')
```

### 2. 가변 인자 리스트

```python
def my_avg(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum/len(args)
```

### 3. 반환값

- ### result에 저장된 값은 None
  
  - `my_func` 함수는 return이 없는 void함수이기 때문에

### 4. 이름 공간(Namespace)

- LEGB
  
  - Local
  
  - Enclosed
  
  - Global
  
  - Built-in

### 5. 매개변수와 인자, 그리고 반환

- (1) 함수는 오직 하나의 객체만 반환할 수 있으므로 `return a,b` 와 같이 쓸 수 없다
  
  - 튜플을 사용하여 반환가능하다.

### 6. 재귀함수

- 장점
  
  1. 변수의 사용이 줄어들고 코드의 가독성이 높아진다.

- 단점
  
  1. 입력 값이 크면 연산속도가 오래 걸린다
