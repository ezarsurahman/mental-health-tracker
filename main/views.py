from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165894',
        'name': 'Ezar Akhdan Shada Surahman Anjrot',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
