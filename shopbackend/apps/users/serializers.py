from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'get_full_name', 'date_of_birth', 'address', 'city', 'postcode', 'phone','roles',)