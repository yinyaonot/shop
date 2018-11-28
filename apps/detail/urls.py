from django.conf.urls import url

from apps.detail import views

'''
url('detail' shop_id)
'''
urlpatterns = [
    url('detail/', views.detail, name='detail'),
    # 动态路由
    # url('detail/<(\w+)/>', views.detail, name='detail'),
]
