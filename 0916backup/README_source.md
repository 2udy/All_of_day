# README

### 작성하면서

- mypjt / urls.py

  `  path('movies', include('moivies.urls'))`

  - `'movies'`
  - `'movies.urls'` 와 `'movies/urls'`의 차이

- html

  - input

    ```html
    # date
    <label for="start">Start date:</label>
    <input type="date" id="start" name="trip-start"
           value="2018-07-22"
           min="2018-01-01" max="2018-12-31">
    
    #url
    <label for="url">Enter an https:// URL:</label>
    <input type="url" name="url" id="url"
           placeholder="https://example.com"
           pattern="https://.*" size="30"
           required>
    
    # select
    <select id="pet-select">
        <option value="">--Please choose an option--</option>
        <option value="dog">Dog</option>
        <option value="cat">Cat</option>
        <option value="hamster">Hamster</option>
        <option value="parrot">Parrot</option>
        <option value="spider">Spider</option>
        <option value="goldfish">Goldfish</option>
    </select> 
    ```

  - a

    ```html
    <p>You can reach Michael at:</p>
    
    <ul>
      <li><a href="https://example.com">Website</a></li>
      <li><a href="mailto:m.bluth@example.com">Email</a></li>
      <li><a href="tel:+123456789">Phone</a></li>
    </ul>
    
    ```

    

  - 

- views.py

  - `render(request, template_name, context)`
    - request: 응답을 생성하는데 사용되는 요청객체
    - template_name: 템플릿의 전체 이름 또는 템플릿 이름의 경로
    - context: 템플릿에서 사용할데이터(dictionary type)
  - `redirect()`
    - 인자에 작성된 곳으로 요청을 보냄
    - view name :  ' articles:index'
    - URL: '/articles'



[해야할 일]

EDIT -  release_date 기존 데이터 출력 (django-filter에서 찾아보기)

`value="{{ movie.release_date|date:"Y-m-d"}}"`







score에 정수만 입력되는 문제 해결 : `type="number" step="0.01"` 기본은 1

----

### 실행하면서

- views.py
  - `  movie.title = request.POST.get('title') `를 `  movie.title = 'title'`로 작성해서 오류발생.
    - `  movie.title = request.POST.get('title') `와`  movie.title = request.GET.get('title') `의 차이점

- index.html

  - `<a href="{% url 'movies:detail' movie.pk %}"> {{ movie.title }} </a>`를

    `<a href="{% url 'movies:detail' %}"> {{ movie.title }} </a>`로 작성해서 오류 발생

    ```
    NoReverseMatch at /movies/
    Reverse for 'detail' with no arguments not found. 1 pattern(s) tried: ['movies/(?P<pk>[0-9]+)/\\Z']
    ```



- form tag method의 기본값은 "GET"



POST와 GET차이: 

render와 redirect : redirect 자리에 render를 쓰면 안되는 이유...? render는  url주소를 보내지 않음.



