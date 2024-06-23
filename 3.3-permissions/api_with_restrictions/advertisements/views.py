from rest_framework import permissions, viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter

class AdvertisementThrottleMixin:
    """Mixin для добавления ограничений на запросы."""

    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_scope = 'advertisements'

class AdvertisementViewSet(AdvertisementThrottleMixin, viewsets.ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        """Создание объявления."""
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        """Обновление объявления."""
        serializer.save(creator=self.request.user)

    def perform_destroy(self, instance):
        """Удаление объявления."""
        instance.delete()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Права доступа для владельцев объявлений."""

    def has_object_permission(self, request, view, obj):
        """Проверка прав на объект."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user
