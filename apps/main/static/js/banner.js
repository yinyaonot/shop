/**
 * 第一步导入插件
 * 第二歩定义 html元素
 * 第三步 实例化swiper对象
 */
$(function () {
    let sp = new Swiper('.swiper-container', {
        //表示轮播的方向水平 也可以是垂直滚动
        direction: 'horizontal',
        //无限轮播  默认是false
        loop: true,
        //定义下圆点
        pagination: {
            //添加小圆点
            el: '.swiper-pagination',
            //点击小圆点切换图片
            clickable: true,
        },
        //设置左右切换按钮
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        autoplay: true,
        delay: 1000,
    })
})


