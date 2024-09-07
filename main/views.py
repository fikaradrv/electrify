from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306203873',
        'name': 'Fikar Hilmi Adhrevi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
