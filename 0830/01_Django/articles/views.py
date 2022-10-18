from email import message
import random
from this import d
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def daeun(request):
    return render(request, 'daeun.html')
    
def greeting(request):
    foods = ['Apple', 'banana', 'orange']
    info = {
        'name': 'Alice',
    }
    context = {
        'info' : info,
        'foods' : foods,

    }
    return render(request, 'greeting.html',context)

def dinner(request):
    foods = ['Apple', 'banana', 'orange']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request,'throw.html')

def cathch(request):
    # # throwd에서 보낸 데이터를 찾아서 저장
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)


def hello(request,name):
    context = {
        'name': name
    }
    return render(request, 'hello.html', context)