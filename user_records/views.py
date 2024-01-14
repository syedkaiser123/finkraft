from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class UserListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating users.

    - For listing users, send a GET request to the endpoint.
    - For creating a new user, send a POST request with user data in the request body.

    Endpoint:
    - GET: /api/users/
    - POST: /api/users/
    """
    serializer_class = UserSerializer
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating products.

    - For listing products, send a GET request to the endpoint.
    - For creating a new product, send a POST request with product data in the request body.

    Endpoint:
    - GET: /api/products/
    - POST: /api/products/
    """
    serializer_class = ProductSerializer
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveView(generics.RetrieveAPIView):
    """
    View for retrieving a single product details using its product ID.

    - For retrieving product details, send a GET request to the endpoint with the product ID.

    Endpoint:
    - GET: /api/products/<product_id>/
    """
    serializer_class = ProductSerializer
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

