import random
from django.shortcuts import render
from .models import User
# Create your views here.

def rnd(request):
    n = random.randint(0,100)
    return render(request, 'rnd.html', {'n':n})

def main(request):
    return  render(request, 'main.html',{})

def stepenRandchisla(request,number):
    user = User()
    user.name = "Vasya"+number
    user.last_name = 'Petrov' + number
    user.password = "123"+number
    user.save()
    number = int(number) if number else 100
    spis=[]
    chis=random.randint(0,int(number))
    for i in range (0,int(number)):
        spis.append(chis**i)
    return  render(request, 'stepenRandchisla.html', {'chis':chis, 'spis':spis})

def MyUsers(request):
    users = User.objects.all()
    return  render(request, 'MyUsers.html', {'users':users})