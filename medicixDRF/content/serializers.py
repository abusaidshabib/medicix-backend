from .models import Category, Subcategory, MainCategory
from rest_framework import serializers

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name']

    def create(self, validated_data):
        sec_category = self.context.get('sec_category')
        sub_category = Subcategory.objects.create(category=sec_category, **validated_data)
        return sub_category

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']

    def create(self, validated_data):
        main_category = self.context.get('main_category')
        removed_maincategory = validated_data.pop('maincategory')
        category = Category.objects.create(maincategory=main_category, **validated_data)
        return category

class MainCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'categories']

    def create(self, validated_data):
        main_category = MainCategory.objects.create(**validated_data)
        return main_category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance