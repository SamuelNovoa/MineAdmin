from django.shortcuts import render


def index(request):
    return render(request, 'views/index.html')


def play(request):
    return render(request, 'views/play.html')


def stats(request):
    return render(request, 'views/stats.html')


def tools(request):
    return render(request, 'views/tools.html')
