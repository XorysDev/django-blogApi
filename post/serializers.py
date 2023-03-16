from rest_framework import serializers
from category.models import Category
from comment.serializers import CommentSerializer
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'category', 'preview', 'owner_username', 'category_name')


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    # comments = CommentSerializer(many=True)  # first method

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['comments_count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance=instance.comments.all(), many=True).data
        return repr


class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'preview')
