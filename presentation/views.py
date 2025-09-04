from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'presentation/404.html', context, status=404)


def error_500(request):
    context = {}
    return render(request, 'presentation/500.html', context, status=500)


def error_403(request, exception):
    context = {}
    return render(request, 'presentation/403.html', context, status=403)


def error_400(request, exception):
    context = {}
    return render(request, 'presentation/400.html', context, status=400)


def robots_txt(request):
    body = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Allow: /static/\n"
    )
    resp = HttpResponse(body, content_type="text/plain; charset=utf-8")
    resp["Cache-Control"] = "public, max-age=3600"
    return resp
