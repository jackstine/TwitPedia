from django.shortcuts import render
from django.views.generic import TemplateView, FormView

class IndexView(FormView):
    template_name = 'news/searchForm.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
