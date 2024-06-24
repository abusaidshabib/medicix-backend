from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Subcategory, MainCategory
from .serializers import MainCategorySerializer, CategorySerializer, SubcategorySerializer
from rest_framework import status, generics

# Create your views here.


class CategoryGetCreateView(APIView):
    def get(self, request):
        main_categories = MainCategory.objects.all()
        serializer = MainCategorySerializer(main_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        category_type = request.data.get('category_type')
        name = request.data.get('name', None)
        main_id = request.data.get('main_id', None)
        cat_id = request.data.get('cat_id', None)
        main_category = None
        sec_category = None

        if main_id is not None:
            try:
                main_category = MainCategory.objects.get(id=main_id)
            except MainCategory.DoesNotExist:
                return Response({'error': 'MainCategory not found'}, status=status.HTTP_404_NOT_FOUND)

        if category_type == 'main':
            serializer = MainCategorySerializer(data=request.data)
        elif category_type == 'cat':
            if main_category is None:
                return Response({'error': 'MainCategory is required for creating a Category'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = CategorySerializer(data=request.data, context={'main_category': main_category})
        elif category_type == 'sub':
            if cat_id is not None:
                try:
                    sec_category = Category.objects.get(id=cat_id, maincategory__id=main_id)
                except Category.DoesNotExist:
                    return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = SubcategorySerializer(data=request.data, context={'sec_category': sec_category})
        else:
            return Response({"error": "Invalid category type"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            if category_type == 'cat':
                serializer.save(maincategory=main_category)
            else:
                serializer.save()
            return Response({"success": True, "category": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        category_type = request.data.get('category_type')
        name = request.data.get('name', None)
        main_id = request.data.get('main_id', None)
        cat_id = request.data.get('cat_id', None)
        sub_id = request.data.get('sub_id', None)
        instance = None

        if main_id is not None:
            try:
                instance = MainCategory.objects.get(id=main_id)
            except MainCategory.DoesNotExist:
                return Response({'error': 'MainCategory not found'}, status=status.HTTP_404_NOT_FOUND)

        if cat_id is not None:
            try:
                instance = Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        if sub_id is not None:
            try:
                instance = Subcategory.objects.get(id=sub_id)
            except Subcategory.DoesNotExist:
                return Response({'error': 'Subcategory not found'}, status=status.HTTP_404_NOT_FOUND)

        if category_type == 'main':
            serializer = MainCategorySerializer(instance, data=request.data)
        elif category_type == 'cat':
            serializer = CategorySerializer(instance, data=request.data)
        elif category_type == 'sub':
            serializer = SubcategorySerializer(instance, data=request.data)
        else:
            return Response({"error": "Invalid category type"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "category": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)