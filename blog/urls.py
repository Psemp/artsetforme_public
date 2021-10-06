from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.BlogpostListView.as_view(), name='actualites')
]
