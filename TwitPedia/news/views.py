from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from common.pages.services.ServicePages import wikiPage, twitterSearchPage
from common.html.services.ServiceHTML import createTwitPediaTable

class IndexView(FormView):
    template_name = 'news/searchForm.html'

    def get(self, request):
        search = request.GET.get("search")
        if (search == None):
            return self.tablePage(request.GET)
        else:
            return self.createTable(search, 1, request)

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
        geo = request.GET.get("geo")
        if (geo != None):
            return self.createTableGeo(search, pageNum, request, response)
        else:
            response["tablePage"] = createTwitPediaTable(pageNum,search)
            return self.action(response)


    def createTableGeo(self, search, pageNum, request, response):
        lat = request.GET.get("lat")
        lon = request.GET.get("long")
        geocode = str(lat) + "," + str(lon) + ",150mi"
        print geocode + "********THIS IS THE GEOCODE ****************"
        response["tablePage"] = createTwitPediaTable(pageNum,search, geocode = geocode)
        return self.action(response)
        

    def action(self, response = {}):
        return self.render_to_response(self.get_context_data(**response))
