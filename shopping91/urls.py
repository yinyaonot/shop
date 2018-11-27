from django.conf.urls import url, include
from django.contrib import admin

from apps.main import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index, name='index'),
    url('account/', include('account.urls')),
    url('cate/', include('cate.urls')),
    url('detail/', include('detail.urls')),
    url('main/', include('main.urls')),
    url('search/', include('search.urls')),
]
