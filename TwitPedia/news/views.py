from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from common.pages.services.ServicePages import wikiPage, twitterSearchPage
from common.html.services.ServiceHTML import createTwitPediaTable

class IndexView(FormView):
    template_name = 'news/searchForm.html'

    def get(self, request, *args, **kwargs):
        response = {}
        search = request.GET.get("search")
        response['search'] = search
        T = request.GET.get("type")
        wikiPageNum = request.GET.get("wiki_page")
        twitPageNum = request.GET.get("twit_page")
        response["show"] = True

        #Table code here
        table = createTwitPediaTable(1,1,"Warren Buffet")
        response["headers"] = table.headers()
        response["rows"] = table.rows()
        if (search == None):
            response["show"] = False
            return self.render_to_response(self.get_context_data(**response))
#        if (T == "w"):
#            response["wikiPages"] = wikiPage(wikiPageNum, search)
#            response['tweetPages'] = twitterSearchPage(1,search)
#        elif (T == "t"):
#            response["wikiPages"] = wikiPage(1, search)
#            response['tweetPages'] = twitterSearchPage(twitPageNum,search)
#        else:
#        response['wikiPages'] = wikiPage(1, search)
#        response['tweetPages'] = twitterSearchPage(1,search)
        return self.render_to_response(self.get_context_data(**response))
