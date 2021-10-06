from django.shortcuts import render


def index(request):
    return render(request, 'presentation/index.html')


def contact(request):
    return render(request, 'presentation/contact.html', context={'title': "Nous Contacter"})


def covidinfo(request):
    return render(request, 'presentation/covidinfo.html', context={'title': "Arts Et Forme - COVID19"})


def stages(request):
    return render(request, 'presentation/stages.html', context={'title': "Nos Stages"})


def team(request):
    return render(request, 'presentation/equipe.html', context={'title': "Notre Équipe"})


def planning(request):
    return render(request, 'presentation/planning.html', context={'title': "Planning et Tarifs"})


def medias(request):
    return render(request, 'presentation/medias.html', context={'title': "Medias"})


def rental(request):
    return render(request, 'presentation/location_salle.html', context={'title': "Location de Salle"})


def legal(request):
    return render(request, 'presentation/legal.html', context={'title': "Mentions Légales"})
