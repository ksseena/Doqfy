from django.shortcuts import render

# Create your views here.
import random
import string
from django.shortcuts import render,redirect,get_object_or_404
from .models import URL

def generate_short_url():
    chars= string.ascii_letters+string.digits
    return ''.join(random.choice(chars) for _ in range(6))
    # if request.method=='POST':

def index(request):
    if request.method==