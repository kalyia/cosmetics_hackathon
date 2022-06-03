from django.urls import path

from apps.category.views import ListCreateCategoryView

urlpatterns = [
    path('list_or_create/', ListCreateCategoryView.as_view()),

]