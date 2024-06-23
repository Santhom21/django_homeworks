from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Review
from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)

class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        mark = request.query_params.get('mark')
        reviews = Review.objects.filter(product_id=product_id, mark=mark) if mark else Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
