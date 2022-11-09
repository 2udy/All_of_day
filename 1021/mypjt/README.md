# DB 설계를 활용한 REST API 설계

### ✍️ 목표

- DRF를 활용한 API Server 제작



### 🔨 사용기술 및 라이브러리

- Django Rest Framework



### 💡 새롭게 알게 된 점

- ##### **[사용자 정의 관계형 필드](https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields)**

  ```python
  class MovieSerializer(serializers.ModelSerializer):
  
      class MovieReviewSerializer(serializers.ModelSerializer):
  
          class Meta:
              model = Review
              fields = ('title', 'content')
      
      class MovieActorSerializer(serializers.ModelSerializer):
  
          class Meta:
              model = Actor
              fields = ('name',)
              
      actors = MovieActorSerializer(many=True, read_only=True)
      review_set = MovieReviewSerializer(many=True, read_only=True)
  
      class Meta:
          model = Movie
          fields = '__all__'
  ```



### :exclamation: 실수

###### models.py

- `on_delete=CASCADE` : :x:

  `on_delete=models.CASCADE` : :o:

- `related_name='movies'`

  - serializer에서 사용하기 위해 필요함.

###### serializers.py

- `read_only_fields = ` :  유효성 검사에서 제외시키고 데이터 조회 시에는 출력



