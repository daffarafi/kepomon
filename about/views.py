from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Kepomon',
        'name': 'About',
        'class': 'PBP A',
    }

    return render(request, "main.html", context)