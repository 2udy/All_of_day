# 0901 homwork(03) 최다은

1. `python manage.py makemigrations`

   `python manage.py migrate `

2. ```python
   # 3
   post = Post('제목', '내용')
   post.save()
   ```

3.  ```python
    # 3
    post3 = Post.objects.all().first()
    ```

4. ```python
   my_post.title = '안녕하세요'
   my_post.content = '반갑습니다'
   my_post.save()
   ```

5. (a) : `objects` 

   (b): `all()`