from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.order import views
from .views import OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="orders")
router.register("orderitems", OrderItemViewSet, basename="orderitems")

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
    path('admin/', include(router.urls)),
]