from django.conf.urls import url

from apps.main import views

urlpatterns = [
    url('index/', views.index, name='index'),
]
