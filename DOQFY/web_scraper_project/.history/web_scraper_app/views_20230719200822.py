from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Nifty50Data

def display_data(request):
    data = Nifty50Data.objects.all()
    return render(request, 'index.html', {'data': data})
