from django.shortcuts import render, redirect

from apps.main.models import *

'''
传参 两种
?
动态路由
'''


def detail(request):
    shop_id = request.GET.get('sid')
    if shop_id:
        try:
            # 返回列表套字典对象
            shops = Shop.objects.filter(shop_id=shop_id).values('shop_id',
                                                                'promote_price',
                                                                'original_price',
                                                                'stock', 'sub_title',
                                                                'name')
            if shops.exists():
                shop = shops.first()
                imgs = ShopImage.objects.filter(shop_id=shop.get('shop_id')).values('shop_img_id', 'type')
                shop.update(imgs=imgs)
                reviews = Review.objects.filter(shop_id=shop_id)
                return render(request, 'detail.html', {'shop': shop, 'reviews': reviews})
        except Exception as e:
            print(e)
    else:
        pass
        return render(request, 'detail.html')
