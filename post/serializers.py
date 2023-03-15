from rest_framework import serializers
from category.models import Category
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'category', 'preview')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'preview')
