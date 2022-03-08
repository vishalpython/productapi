from django.urls import include,path
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from Product import views

router = DefaultRouter()
router.register('products',views.ProductViewset,basename='product')

urlpatterns = [
    path('',include(router.urls)),
    #path('product-list/',views.ProductApiView().as_view()),
    #path('product-list/<int:pk>',views.ProductApiView().as_view())
]
