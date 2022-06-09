from django.urls import path

from apps.product.views import * 


urlpatterns = [
    path('', ListCreateProductView.as_view()),
    path('list_or_create/', ListCreateProductView.as_view()),
    path('update/<int:pk>/', UpdateProductView.as_view()),
    path('<int:pk>/', GetProductView.as_view()),
    path('<int:pk>/like/', LikeProductView.as_view()),
    path('delete/<int:pk>/', DestroyProductView.as_view()),

    

] 