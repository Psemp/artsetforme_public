"""artsetforme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from presentation import views as pres_views
from download import views as download_views


urlpatterns = [
    path('actualites/', include('blog.urls', namespace="actualites")),
    path('admin/', admin.site.urls),
    path('location_salle', pres_views.rental, name="location_salle"),
    path('', pres_views.index, name='index'),
    path('contact/', pres_views.contact, name='contact'),
    path('mentions-legales/', pres_views.legal, name='mentions-legales'),
    path('equipe/', pres_views.team, name='equipe'),
    path('stages/', pres_views.stages, name='stages'),
    path('documents/', download_views.documents, name='documents'),
    path('medias/', pres_views.medias, name='medias'),
    path('planning-et-tarifs/', pres_views.planning, name='planning-et-tarifs'),
    path("robots.txt", pres_views.robots_txt, name="robots_txt"),
]

handler404 = pres_views.error_404

handler500 = pres_views.error_500

handler403 = pres_views.error_403

handler400 = pres_views.error_400

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
