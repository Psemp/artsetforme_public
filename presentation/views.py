from django.shortcuts import render


def index(request):
    return render(request, 'presentation/index.html')


def contact(request):
    return render(request, 'presentation/contact.html', context={'title': "Nous Contacter"})


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


def error_404(request, exception):
    context = {}
    return render(request, 'presentation/404.html', context)


def error_500(request):
    context = {}
    return render(request, 'presentation/500.html', context)


def error_403(request, exception):
    context = {}
    return render(request, 'presentation/403.html', context)


def error_400(request, exception):
    context = {}
    return render(request, 'presentation/400.html', context)
