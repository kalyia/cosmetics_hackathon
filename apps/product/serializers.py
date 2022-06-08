from rest_framework import serializers
from apps.product.models import Product, LikeProduct, Review


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["category"] = instance.category.name
        rep["likes"] = instance.likes.all().count()
        rep['reviews'] = instance.reviews.all().count()
        return rep


class LikeProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = LikeProduct
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('author', )

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.name
        representation['author'] = instance.author.email
        return representation

