from django.shortcuts import render, redirect
from app.models import notes
import datetime
from django.shortcuts import get_list_or_404



def home(request):
    context = {
        'notes': notes.objects.all(),
    }
    return render(request, 'app/home.html', context)


def add_note(Request):
    if Request.method == 'POST':
        title = Request.POST['title']
        note = Request.POST['message']
        p = notes(title= title, note= note)
        p.save()   
        return redirect('home')
    
    return render(Request, 'app/add.html')


def detail_nots(Request, pk):
    context = {
        'edit': get_list_or_404(notes, id=pk),
    }
    return render(Request, 'app/edit.html', context)




