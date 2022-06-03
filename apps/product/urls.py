from django.urls import path

from apps.product.views import ListCreateProductView, GetProductView, LikeProductView

urlpatterns = [
    path('list_or_create/', ListCreateProductView.as_view()),
    path('<int:pk>/', GetProductView.as_view()),
    path('<int:pk>/like/', LikeProductView.as_view()),

]