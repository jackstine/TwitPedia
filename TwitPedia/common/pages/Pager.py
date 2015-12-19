from django.core.paginator import *

def getPages(page, objs, numOnPage = 10):
    paginator = Paginator(objs,numOnPage)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = pageinator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)
    return objs
