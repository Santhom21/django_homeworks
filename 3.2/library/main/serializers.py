from rest_framework import serializers
from .models import Book, Order

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Дополнительное задание: добавление поля orders_count
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = instance.order_set.count()
        return representation

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # Дополнительное задание: добавление поля books
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = BookSerializer(instance.books.all(), many=True).data
        return representation
