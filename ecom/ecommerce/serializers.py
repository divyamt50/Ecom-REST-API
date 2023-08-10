from rest_framework import serializers
from ecommerce.models import Category, Products

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    cat_id = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = "__all__"

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    prod_id = serializers.ReadOnlyField()
    class Meta:
        model = Products
        fields = '__all__'