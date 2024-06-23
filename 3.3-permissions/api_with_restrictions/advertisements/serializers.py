# advertisements/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement, AdvertisementStatusChoices  # добавлен импорт

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)

class AdvertisementSerializer(serializers.ModelSerializer):
    """Сериализатор для объявления."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at',)
        read_only_fields = ('creator',)

    def validate(self, data):
        """Валидация при создании или обновлении объявления."""

        # Проверяем, что у пользователя не больше 10 открытых объявлений
        user = self.context['request'].user
        open_ads_count = Advertisement.objects.filter(creator=user, status=AdvertisementStatusChoices.OPEN).count()

        if self.instance is None and open_ads_count >= 10:
            raise serializers.ValidationError("Превышен лимит открытых объявлений (максимум 10).")

        return data
