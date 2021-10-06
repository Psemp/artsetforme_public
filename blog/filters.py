import django_filters
from django import forms

from backoffice.models import Topic


class BlogpostFilter(django_filters.FilterSet):

    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Topic.objects.all(),
        label='Filtrer par categorie',
        widget=forms.CheckboxSelectMultiple()
    )
