from django.shortcuts import render
from ..models import UserStat

from mineAdmin.services import ServerService


def index(request):
    return render(request, 'views/index.html')


def play(request):
    server = ServerService()
    return render(request, 'views/play.html', {
        'available': server.available,
        'has_mods': server.has_mods,
        'mods_list': server.enabled_mods
    })


def stats(request):
    records = UserStat.objects.all()

    statistics = {
        'labels': [data.month for data in records],
        'players': [data.avg_users for data in records],
        'registers': [data.avg_new_users for data in records]
    }

    return render(request, 'views/stats.html', {'statistics': statistics})


def tools(request):
    return render(request, 'views/tools.html')
