from django.urls import path, include
from rest_framework import routers
from ecommerce.views import CategoryViewSet, ProductViewSet, SendOTPView, VerifyOTPView

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('send_otp/', SendOTPView.as_view(), name='send_otp'),
    path('verify_otp/', VerifyOTPView.as_view(), name = 'verify_otp'),
    path('', include(router.urls))
]
