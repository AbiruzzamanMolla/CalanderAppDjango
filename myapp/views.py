from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from myapp.models import Enrty
from myapp.forms import EntryForm


def index(request):
    entries = Enrty.objects.all()
    return render(request, 'myapp/index.html', {'entries': entries})


def details(request, pk):
    enrty = Enrty.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry': enrty})


def add(request):

    if request.method == 'POST':

        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Enrty.objects.create(
                name=name,
                date=date,
                description=description,
            ).save()

            return HttpResponseRedirect('/')
    else:
        form = EntryForm
    return render(request, 'myapp/form.html', {'form': form})


def delete(request, pk):

    if request.method == "DELETE":
        entry = get_object_or_404(Enrty, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')
