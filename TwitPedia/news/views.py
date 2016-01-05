from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from common.pages.services.ServicePages import wikiPage, twitterSearchPage
from common.html.services.ServiceHTML import createTwitPediaTable

class IndexView(FormView):
    template_name = 'news/searchForm.html'
    form_class = dict

    def get(self, request):
        get = request.GET
        search = get.get("search")
        if (search == None):
            return self.tablePage(get)
        else:
            return self.createTable(search, 1, get)

    def tablePage(self, request):
        tablePage = request.get("tablePageNum")
        search = request.get("tablePageSearch")
        if (tablePage == None):
            return self.action()
        else:
            return self.createTable(search, tablePage, request)

    def createTable(self, search, pageNum, request):
        response = dict()
        response["show"] = True
        geo = request.get("geo")
        if (geo != None):
            return self.createTableGeo(search, pageNum, request, response)
        else:
            response["tablePage"] = createTwitPediaTable(pageNum,search)
            return self.action(response)


    def createTableGeo(self, search, pageNum, request, response):
        lat = request.get("lat")
        lon = request.get("long")
        geocode = str(lat) + "," + str(lon) + ",150mi"
        response["tablePage"] = createTwitPediaTable(pageNum,search, geocode = geocode)
        return self.action(response)
        

    def action(self, response = {}):
        context = self.get_context_data(**response)
        return self.render_to_response(context)
