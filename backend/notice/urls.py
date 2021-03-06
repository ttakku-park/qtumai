"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
CouponManageViewSet, FAQFormViewSet, NoticeViewSet, ProposeBusinessViewSet, ProposeGoodShopViewSet, business_create
)

router = DefaultRouter(trailing_slash=True)
router.register(r"business/coupon", CouponManageViewSet, basename="business/coupon")
router.register(r"propose/goodshop", ProposeGoodShopViewSet, basename="propose/goodshop")
router.register(r"propose/business", ProposeBusinessViewSet, basename="propose/business")
router.register(r"notice", NoticeViewSet, basename="notice")
router.register(r"faq", FAQFormViewSet, basename="faq")

urlpatterns = [
    path('business/register', business_create)
]+ router.urls
