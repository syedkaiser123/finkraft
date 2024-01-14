from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']

    def validate_price(self, value):
        # Custom validation for the 'price' field
        if value < 0:
            raise serializers.ValidationError("Price must be a non-negative value.")
        return value

