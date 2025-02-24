from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    dct = {
        'obj': {
        'Car': 'BMW',
        'Owner': 'Emin',
        'MarketCap': '3.000.000$',
        'title': 'Главная страница!!'
        }
    }
    return render(request, 'main/index.html', dct)

def about(request):
    return render(request, 'main/about.html')