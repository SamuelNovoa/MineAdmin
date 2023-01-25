from django.shortcuts import render


def index(request, error=None):
    print(error)
    return render(request, 'views/index.html', {'error': error})


def play(request):
    return render(request, 'views/play.html', {'error': False})


def stats(request):
    return render(request, 'views/stats.html')


def tools(request):
    return render(request, 'views/tools.html')
