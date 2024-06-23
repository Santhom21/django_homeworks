from django.contrib import admin
from django.urls import path
from main.views import products_list_view, ProductDetailsView, ProductFilteredReviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products_list_view),
    path('products/<int:product_id>/', ProductDetailsView.as_view()),
    path('products/reviews/<int:product_id>/', ProductFilteredReviews.as_view())
]
