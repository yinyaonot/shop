from django.conf.urls import url

from apps.search import views

urlpatterns = [
    url('search/', views.search_result, name='search')
]
