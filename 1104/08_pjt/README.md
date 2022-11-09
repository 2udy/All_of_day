# README

- ### 추천 알고리즘 

  평점이 8.5 이상인 영화중에 10편을 랜덤으로 추천한다.

- ### 협업하며 느낀점

  - ##### 다은

    혼자 할 때 보다 집중이 잘 된다. 다른 조 사람들이 쉬질 않아서 쉬는 시간에 심심하다. 평소보다 말을 많이 해서 목이 아프다. 생각하지 못한 부분을 고민해 볼 수 있어서 좋다.
    그 동안 프레임워크와 언어를 익히는 것을 목표로 하는 프로젝트를 진행해 와서 그런지 알고리즘 수업과 웹 수업이 별개의 문제처럼 느껴졌는데, 오늘 프로젝트를 진행하며 두 부분이 합쳐지는 포인트를 알 수 있었다. 

  - ##### 유태

    첫 팀프로젝트라 민폐를 끼칠까봐 걱정했는데 다행이 내가 너무 모르지는 않았다. 그렇다고 잘 알지도 못해 종종 당황하는 순간이 있었다. 그때마다 팀원이 해결책을 내주어서 프로젝트를 수월하게 해결할 수 있었다.  views에서 파이썬 알고리즘을 통해 데이터 처리를 했다. 지금은 문제없이 해결됐지만 나중에 데이터의 양이 많아지면 시간복잡도가 매우클것이 당연하기 때문에, 알고리즘 공부도 쉬지 않고 해야겠다고 다시금 깨달았다. 최근에 vue에만 집중하다보니 벌써 django와 axios에 대해 까먹은 것이 많다. 수업 후와 주말을 이용해 최종 프로젝트 전까지 열심히 공부해야겠다.

- ### 실수

#### 1. genre

​	Movie모델의 genres 컬럼은 Genre모델과 M:N 관계이다. 때문에 Movie모델에서 genres 값을 사용하기 위해선 Genre모델을 참조해야 한다.

```python
## movies/views.py

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = movie.genres.all()
    context = {
        'movie': movie,
        'genres': genres
    }
    return render(request,'movies/detail.html',context)
```

위와 같이 `genres = movie.genres.all() `을 사용하여 한개의 영화에 저장된 장르 쿼리셋을 얻을 수 있었다.

```html
movies/detail.html

<p>장르:
  {% for genre in genres %}
  {{ genre.name }}
  {% endfor %} 
</p>
```

for 구문을 이용해 각각의 장르 쿼리를 추출하였고, 추출한 genre의 name값을 출력하여 문제에서 요구하는 영화의 장르 값을 얻을 수 있었다.

다대다 관계에선 참조 또는 역참조를 통하여 원하는 쿼리셋을 가져와야 하고, 그 쿼리셋의 객체에 하나씩 접근하여 원하는 데이터 값을 추출해야 한다.

#### 2. random_good_movie

우리조는 recommended 페이지의 추천 기준을 '평점 8.5 이상인 영화중 랜덤 10개'로 선정했다.

우리가 정한 기준을 충족하는 영화를 추출하는 것이 고민이 되었고, 이를 html이 아니라 우리가 익숙한 python으로 해결하기로 했다.

```python
# movies/views.py

import random

@require_safe
def recommended(request):
    # 무비 다 받아서
    # 평점 8.5 이상인거 골라내서 AJAX로 넘겨준다.
    movies = Movie.objects.all()
    good_movies = []
    for i in range(len(movies)):
        if movies[i].vote_average >= 8.5:
            good_movies.append(movies[i])
    random_good_movies = random.sample(good_movies, 10)
    context = {
        'random_good_movies': random_good_movies
    }
    return render(request, 'movies/recommended.html', context)
```

for문과 if문을 사용하여 평점 8.5이상인 영화가 담긴 good_movies 리스트를 만들었다. 이후에 random모듈을 사용하여 good_movies에서 랜덤으로 10개의 영화를 추출한 random_good_movies를 만들었다.

`random_good_movies = random.sample(good_movies, 10)` 

조건 처리를 views.py에서 전부 진행한 후 html로 넘겨 주었기 때문에, recommended.html에서는 이를 출력하기만 하면 됐다.

views.py에서 파이썬 문법을 통해 쉽게 원하는 데이터를 추출할 수 있다는 것을 알게되었다. 그러나 만약 movies 테이블이 수천, 수만개가 넘는 많은 데이터를 가지고 있다면, 위와같은 코드는  데이터를 처리하는데 큰 시간을 소요하게 될 것이고, 이는 사용자에게 불편함을 줄 것이다. 이러한 문제를 해결하기위해 실무에서 직접적으로 적용되는 기술스택 뿐만 아니라 알고리즘 공부도 꾸준히 해야겠다고 생각했다.



#### 3. AJAX

1. follow

   - **axios**

     ###### 구조

     ```
     axios(요청할 URL)
     .then(성공하면 수행할 콜백함수)
     .catch(실패하면 수행할 콜백함수)
     ```

     ###### .then((response) => { })

     ​	응답 객체를 인자로 하는 콜백함수를 작성

     ###### .catch((response) => {})

     ​	응답 객체는 오류에 대한 정보를 담고 있다.

2. like

   - **각각의 form을 다르게 선택하는 방법**

     `  const likeForms = document.querySelectorAll('#like-form')`: :o:

     `  const likeForm = document.querySelector('#like-form')`: :x:
     두번째 처럼 작성하면 id가 `like-form`를 만족하는 첫번째 버튼만 선택 된다.

     전체를 선택하고, `forEach`를 이용하여 조건에 맞는(현재 좋아요를 누르려는) 게시글의 버튼을 선택한다.