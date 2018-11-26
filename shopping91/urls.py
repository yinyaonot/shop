from django.conf.urls import url, include
from django.contrib import admin

from main import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',views.home,name='home'),
    url('account/',include('account.urls')),
    url('cate/', include('cate.urls')),
    url('detail/', include('detail.urls')),
    url('main/', include('main.urls')),
    url('search/', include('search.urls')),
]
