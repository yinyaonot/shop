from django.shortcuts import render
from django.views.decorators.cache import cache_page

from apps.main.models import *


# 缓存
# @cache_page(20)
def index(request):
    nav_list = Navigation.objects.all()
    cate_list = Category.objects.all()
    banner_list = Banner.objects.all()
    for cate in cate_list:
        shops = cate.shop_set.all()
        for shop in shops:
            # shop.img = shop.shopimage_set.values_list('shop_img_id', flat=True).first()
            shop.img = shop.image_set.values_list('shop_img_id',flat=True).first()
        cate.shops = shops

    return render(request, 'index.html', locals())


# def index(request):
#     nav_list = Navigation.objects.all()
#     cate_list = Category.objects.all()
#     banner_list = Banner.objects.all()
#     for cate in cate_list:
#         #  查询分类信息下的所有的商品信息
#         shops = cate.shop_set.all()
#         for shop in shops:
#             # 查询商品的图片信息
#             # values_list  [(626,),(647,)]
#             #  单值   flat=True  [626,647]
#             # [(626,1,'type'),]
#             # values [{shop_img_id:626}]
#             # shop.img = shop.shopimage_set.values('shop_img_id').first()
#             #
#             shop.img = shop.shopimage_set.values_list('shop_img_id', flat=True).first()
#             # shop.img = shop.shopimage_set.values_list('shop_img_id', 'shop_id', 'type')
#             print(shop.img)
#         cate.shops = shops
#
#     return render(request, 'index.html', locals())
