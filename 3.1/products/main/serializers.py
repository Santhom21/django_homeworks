from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    mark_display = serializers.CharField(source='get_mark_display', read_only=True)

    class Meta:
        model = Review
        fields = ('text', 'mark', 'mark_display', 'created_at')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price')


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'reviews')
