from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from apps.product.models import Product, LikeProduct
from apps.product.paginations import ProductPagination
from apps.product.serializers import ProductSerializer, LikeProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ListCreateProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_published", "title"]
    ordering_fields = ['update_date']

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_serializer_context(self):
        return super().get_serializer_context()


class GetProductView(APIView):
    """добавление счетчика просмотров"""

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.watch += 1
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class LikeProductView(APIView):
    """ставить лайки"""

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = request.user
        product = get_object_or_404(Product, pk=pk)
        like, create = LikeProduct.objects.get_or_create(user=user, product=product)
        if like.is_like:
            like.is_like = False
            like.save()
        else:
            like.is_like = True
            like.save()
        serializer = LikeProductSerializer(like)
        return Response(serializer.data)

