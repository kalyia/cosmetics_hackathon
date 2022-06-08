from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.category.models import Category
from apps.category.permissions import IsAdminOrAllowAny
from apps.category.serializers import CategorySerializer


class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrAllowAny,)
