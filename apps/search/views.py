from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from apps.main.models import Shop


def search_result(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        info = request.POST.get('info')
        try:
            shops_search = Shop.objects.filter(Q(name__contains=info) | Q(sub_title__contains=info)).values()
            if shops_search:
                for shop in shops_search:
                    shop.img = shop.shopimage_set.values_list('shop_img_id', flat=True).first()
                return render(request, 'index.html', {'shops_search': shops_search})
            else:
                msg = '无该商品信息'
                return render(request, 'index.html', {'msg': msg})
        except Exception as e:
            return redirect('/')

