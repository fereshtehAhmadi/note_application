from django.shortcuts import render, redirect
from app.models import Notes, Categorie
from django.shortcuts import get_list_or_404, get_object_or_404



def home(request, order=None):
    if order:
        context = {
            'notes': Notes.objects.order_by(order),
        }    
    else:
        context = {
            'notes': Notes.objects.all(),
        }
    return render(request, 'app/home.html', context)


def category(request, cats):
    obj = Categorie.objects.get(category= cats)
    context = {
        'notes': get_list_or_404(Notes, category= obj.id),
    }
    return render(request, 'app/home.html', context)


def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        note = request.POST['message']
        category = request.POST['category']
        if Categorie.objects.filter(category=category).exists() == False:
            Categorie.objects.create(category= category)
        obj = Categorie.objects.get(category= category)
        Notes.objects.create(title= title, note= note, category= obj)
        return redirect('home')
    
    return render(request, 'app/add_edit.html')


def edit_note(request, pk):
    if request.method == 'POST':
        obj = Notes.objects.get(id=pk)
        obj.title= request.POST['title']
        obj.note= request.POST['message']
        category = request.POST['category']
        if Categorie.objects.filter(category=category).exists() == False:
            c = Categorie(category= category)
            c.save()
        cat = Categorie.objects.get(category= category)
        obj.category = cat
        obj.save()   
        return redirect('home')   
    
    context = {
        'notes': get_object_or_404(Notes, id=pk),
    }
    return render(request, 'app/add_edit.html', context)


def detail_nots(request, pk):   
    context = {
        'note': get_list_or_404(Notes, id=pk),
    }
    return render(request, 'app/detail.html', context)


def delete_note(request, pk):
    obj = get_object_or_404(Notes, id=pk)
    
    if request.method == 'POST':
        # id = request.POST['id']
        obj.delete()
        return redirect('home')
    
    context = {
        'delete': obj,
    }
    return render(request, 'app/delete.html', context)
