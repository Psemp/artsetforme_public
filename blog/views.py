from django.views import View
from django.views.generic import ListView

from .models import Blogpost
from .filters import BlogpostFilter


class BlogpostListView(ListView):
    model = Blogpost
    template_name = 'blog/actualites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BlogpostFilter(self.request.GET, queryset=self.get_queryset())
        return context
