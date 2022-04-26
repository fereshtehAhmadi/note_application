from django.shortcuts import render, redirect
from app.models import notes
import datetime
from django.shortcuts import get_list_or_404



def home(request):
    context = {
        'notes': notes.objects.all(),
    }
    return render(request, 'app/home.html', context)


def add_note(request):
    if request.method == 'POST':
        title = Request.POST['title']
        note = Request.POST['message']
        p = notes(title= title, note= note)
        p.save()   
        return redirect('home')
    
    return render(request, 'app/add.html')


def detail_nots(request, pk):
    if request.method == 'POST':
        obj = notes.objects.get(id=pk)
        obj.title= request.POST['title']
        obj.note= request.POST['message']
        obj.save()
        return redirect('home')
        
    context = {
        'notes': get_list_or_404(notes, id=pk),
    }
    return render(request, 'app/detail.html', context)

def delete_note(request, pk):
    if request.method == 'POST':
        obj = notes.objects.get(id=pk)
        obj.delete()
        return redirect('home')
    context = {
        'delete': get_list_or_404(notes, id=pk),
    }
    return render(request, 'app/delete.html', context)
