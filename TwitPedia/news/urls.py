from django.conf.urls import url, patterns

from .views import IndexView

urlpatterns = patterns('',
    url(r'^search/', IndexView.as_view(), name = 'search'),
)
