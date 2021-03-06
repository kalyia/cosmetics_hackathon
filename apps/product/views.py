from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.product.models import Product, LikeProduct,Review
from apps.product.paginations import ProductPagination
from apps.product.serializers import ProductSerializer, LikeProductSerializer, ReviewSerializer
from .permissions import IsAuthororAdminPermission


class ListCreateProductView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, filters.SearchFilter]
    filterset_fields = ["created", "name"]
    ordering_fields = ['price']
    search_fields = ['name', 'slug']

    def get_serializer_context(self):
        return super().get_serializer_context()


class GetProductView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LikeProductView(APIView):

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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
    
        return [IsAuthororAdminPermission()]
        

class DestroyProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
