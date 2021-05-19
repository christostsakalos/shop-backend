
from rest_framework import serializers

from .models import Order, OrderItem
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

from apps.product.serializers import ProductSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    items = MyOrderItemSerializer(many=True)
    fullname = serializers.ReadOnlyField(source='user.get_full_name')
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            'fullname',
            "email",
            "address",
            "postcode",
            "phone",
            "items",
            'paid_status',
            'status',
            "paid_amount"
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),read_only=False)
    fullname = serializers.ReadOnlyField(source='user.get_full_name')

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            'fullname',
            "email",
            "address",
            "postcode",
            "phone",
            "items",
            'status',
            "paid_amount"
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order