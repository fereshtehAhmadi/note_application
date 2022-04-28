from django.shortcuts import render, redirect
from app.models import Notes
import datetime
from django.shortcuts import get_list_or_404



def home(request):
    context = {
        'notes': Notes.objects.all(),
    }
    return render(request, 'app/home.html', context)


def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        note = request.POST['message']
        p = Notes(title= title, note= note)
        p.save()   
        return redirect('home')
    
    return render(request, 'app/add.html')


def detail_nots(request, pk):
    if request.method == 'POST':
        obj = Notes.objects.get(id=pk)
        obj.title= request.POST['title']
        obj.note= request.POST['message']
        obj.save()
        return redirect('home')
        
    context = {
        'notes': get_list_or_404(Notes, id=pk),
    }
    return render(request, 'app/detail.html', context)

def delete_note(request, pk):
    if request.method == 'POST':
        obj = Notes.objects.get(id=pk)
        obj.delete()
        return redirect('home')
    context = {
        'delete': get_list_or_404(Notes, id=pk),
    }
    return render(request, 'app/delete.html', context)
