from django.conf.urls import url, include
import xadmin

from apps.main import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('^$', views.index, name='index'),
    url('account/', include('account.urls')),
    url('cate/', include('cate.urls')),
    url('detail/', include('detail.urls')),
    url('main/', include('main.urls')),
    url('search/', include('search.urls')),
]
