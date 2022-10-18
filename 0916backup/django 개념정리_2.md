# urls

- `path('', views)`

# views

- `render(request, template_name, context)`
  - `request` : 응답을 생성하는 데 사용되는 요청 객체
  - `template_name`: 템플릿의 전체 이름 또는 템플릿 이름의 경로
  - `context`: 템플릿에서 사용할 데이터(딕셔너리 타입)



# templates

- `<form action='#' method='#'> </form>`
  - `action`: 입력 데이터가 전송될 url 지정
  - `method`: 보낼 방법 정의
    - `GET`: R
    - `POST`:C, U, D
- 