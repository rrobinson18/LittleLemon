from rest_framework import serializers
from .models import MenuItem



class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['url', 'username', 'email', 'groups']

# class BookingSerializer(serializers.ModelSerializer): 
#         model = Booking 
        
        