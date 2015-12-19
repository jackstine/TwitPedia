from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from common.pages.services.ServicePages import wikiPage

class IndexView(FormView):
    template_name = 'news/searchForm.html'

    def get(self, request, *args, **kwargs):
        response = {}
        search = request.GET.get("search")
        response['search'] = search
        T = request.GET.get("type")
        if (T == "w"):
            pageNum = request.GET.get("wiki_page")
            response["wikiPages"] = wikiPage(pageNum, search)
        else:
            response['wikiPages'] = wikiPage(1, search)
        return self.render_to_response(self.get_context_data(**response))
