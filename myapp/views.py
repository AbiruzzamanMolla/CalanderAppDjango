from django.shortcuts import render
from myapp.models import Enrty


def index(request):
    entries = Enrty.objects.all()
    return render(request, 'myapp/index.html', {'entries': entries})
