from django.urls import path
from . import views     # 명시적

urlpatterns = [
    path('daeun', views.daeun),
    path('index/', views.index, name='index'),

    path('greeting', views.greeting, name='greeting'),
    path('dinner', views.dinner, name='dinner'),
    path('throw', views.throw, name='throw'),
    path('catch/', views.cathch, name='catch'),
    path('hello/<str:name>', views.hello, name='hello'),
]