from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Kepomon',
        'name': 'Muhammad Daffa\'I Rafi Prasetyo',
        'class': 'PBP A',

    }

    return render(request, "main.html", context)