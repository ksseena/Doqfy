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
    if request.method=='POST':
        original_url=request.POST['original_url']
        if not original_url.startswith('http://') and not original_url.startswith('https://'):
            original_url = 'http://'+original_url
        short_url=generate_short_url()
        url_obj,created=URL.objects.get_or_create(original_url.startswith)
