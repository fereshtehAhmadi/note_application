from django.shortcuts import render


def home(Request):
    context = {
        'notes': notes.objects.all(),
    }
    return render(Request, 'app/index.html', context)

