from rest_framework import serializers
from apps.product.models import Product, LikeProduct


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["category"] = instance.category.title
        rep["likes"] = instance.likes.all().count()
        return rep


class LikeProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = LikeProduct
        fields = "__all__"

