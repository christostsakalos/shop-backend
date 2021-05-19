
from django.urls import path, include
from apps.product import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ParentcategoryViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("categories", CategoryViewSet, basename="categories")
router.register("parentcategories", ParentcategoryViewSet, basename="parentcategories")


urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('parentcategories/', views.ParentCategoriesList.as_view()),
    path('parentcategories/<slug:parentcategory_slug>/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('parentcategories/<slug:parentcategory_slug>/', views.ParentcategoryDetail.as_view()),
    path('parentcategories/<slug:parentcategory_slug>/<slug:category_slug>/', views.CategoryDetail.as_view()),
    #Admin
    path('admin/', include(router.urls))
]