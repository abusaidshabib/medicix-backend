from .models import Category, Subcategory, MainCategory
from rest_framework import serializers

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id','name']

    def create(self, validated_data):
        sec_category = self.context.get('sec_category')
        sub_category = Subcategory.objects.create(category=sec_category, **validated_data)
        return sub_category

class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategory']

    def create(self, validated_data):
        main_category = self.context.get('main_category')
        removed_maincategory = validated_data.pop('maincategory')
        category = Category.objects.create(maincategory=main_category, **validated_data)
        return category


class MainCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    # category = serializers.SerializerMethodField('get_category')
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'category']

    def create(self, validated_data):
        main_category = MainCategory.objects.create(**validated_data)
        return main_category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    # def get_category(self, obj):
    #     # return CategorySerializer(obj.category_set.all(), many=True).data
    #     return CategorySerializer(Category.objects.filter(maincategory=obj), many=True).data






"""
{
    "category_type": "main",
    "name":"Electronics category test 2"
}

{
    "category_type": "cat",
	"main_id": 1,
	"name":"Computer"
}

{
  "category_type": "sub",
	"main_id": 1,
    "cat_id":1,
	"name":"Electronics category 1"
}

# For update related work
{
    "category_type":"main",
    "main_id":1,
    "name":"Electronics update"
}

{
  "category_type": "cat",
    "cat_id":1,
	"name":"Electronics update cat"
}

{
  "category_type": "sub",
    "sub_id":1,
	"name":"Electronics update sub"
}


[
    {
    "name":"main category",
    }
    "category":[
    {
            "name":"category"
        "sub-category":[
            {
            "name":"sub category"
            }
        ]
        }
    ]
]
"""

