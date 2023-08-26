from django.shortcuts import render
from .models import Downloadable


def documents(request):
    file_list = Downloadable.objects.all().order_by('date_uploaded')
    download_links = []
    for item in file_list:
        download_links.append(item)

    download_links.reverse()

    context = {
        "title": "Téléchargements",
        "download_links": download_links
        }

    return render(request, 'download/documents.html', context)
