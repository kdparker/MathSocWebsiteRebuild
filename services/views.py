from __future__ import unicode_literals
from django.shortcuts import render

def home(request):
    return render(request, 'services/index.html')
