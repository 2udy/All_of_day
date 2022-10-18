1. forms 생성
2. new + create 합친 view함수 생성
   1. method 구분 _POST:  작성( 구 create) / GET: 조회( 구 new) 
   2. 요청 받고 유효성 검사 저장 리턴
3. html 수정: {{ form.as_p }}





migrate 전에 user 모델 먼저 만들기

내부 기본주소 값이 accounts로 설정되어 있는 것이 많다.

AbstractUser 상속 받아서 models.py에 User클래스 만들기

AUTH_USER_MODEL = 'accounts.User' 우리가 만든 accounts앱의 User 클래스를 기본 모델로 사용하겠다.라고 세팅

admin.py에서  admin.site.register(User, UserAdmin)

forms.py 에 CustomUserCreationForm(UserCreationForm), CustomUserChangeForm(UserChangeForm)

유연성을 위해 User 직접 참조 보다는 get_user_model 함수 사용



modelForm의 첫번째 인자는 데이터 / Form 의 첫번째 인자는 request





질문!!!:

models.py 에

```
def __str__
```

