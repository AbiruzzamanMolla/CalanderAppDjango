from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from myapp.models import Enrty
from myapp.forms import EntryForm


def index(request):
    return render(request, 'myapp/index.html')

@login_required
def calander(request):
    entries = Enrty.objects.filter(author=request.user)
    return render(request, 'myapp/calander.html', {'entries': entries})

@login_required
def details(request, pk):
    enrty = Enrty.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry': enrty})

@login_required
def add(request):

    if request.method == 'POST':

        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Enrty.objects.create(
                name=name,
                author=request.user,
                date=date,
                description=description,
            ).save()

            return HttpResponseRedirect('/calander')
    else:
        form = EntryForm
    return render(request, 'myapp/form.html', {'form': form})

@login_required
def delete(request, pk):

    if request.method == "DELETE":
        entry = get_object_or_404(Enrty, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/calander')

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calandar')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})