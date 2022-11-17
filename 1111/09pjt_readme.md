#### git을 활용한 협업

- 오늘 git을 활용해 협업을 하며 항상 이해가 잘 안됐던 git과 github 개념 구분이 명확해졌다
- 로컬 브랜치 만들어서 git commit하고 push 하는 법, 깃헙에 요청 올리는 법, master에서 pull 하는 순서를 익힐 수 있었다.
- node_modules 폴더랑 `env.local` 커밋할 때 지울 필요 없다. (`.gitignore`가 자동으로 걸러줌)



#### 최고평점영화 출력

- component에 Bootstrap Grid cards 적용하는 방법을 잘 몰랐다.

  - 아이템에서 카드 적용 따로 해야함

    ###### /MovieView.vue

    ```html
    <div class="row row-cols-1 row-cols-md-3 g-4">
    	<MovieCard/>
    </div>
    ```

    ###### /MovieCard

    ```html
     <div class="col">
        <div class="card" style="height:1000px;">
          <img :src="`https://image.tmdb.org/t/p/original${this.movie.poster_path}`" alt="movie img" style="width:auto;">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    ```

- 영화 포스터 이미지 가져올 때 `src`에 v-bind를 안해서 링크를 제대로 가져오지 못하는 실수를 했다.

  

#### API

- API 가져와서 사용하는 방법을 알게 되었다.
  - axios로 url 받아서 Vuex에 저장한다.
  - params 변수를 선언해 받아야하는 인자를 저장한다.
  - `env.local`에 키를 저장한다.



#### 보고싶은 영화 등록 및 삭제하기

- 그냥 상위 컴포넌트에 저장한 데이터를 사용하려다가 시청 완료 값을 변경하는 과정이 너무 헷갈려서 Vuex에 작성한 영화 목록을 저장해서 활용했다.



