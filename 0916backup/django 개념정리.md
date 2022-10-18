temlpates / urls.py

```python
from django.urls import path, include
path('articles/', include('articles.urls')),
```

articles/ urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [

]
```

articles/tmplates/index.html

```python
{% for article in articles %}     
    ...
{% endfor %}
```





redirect : urls.py에서 요청해라



article.pk 까먹진

```    html
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
```