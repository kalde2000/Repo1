from rest_framework import serializers
from .models import User, Category, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['parent', 'name', 'items_count', 'children_count',]

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Item
        fields = ['name', 'owner', 'category', 'price', 'description', 'photo',
                  'count_views', 'created_at',]
