from rest_framework import generics, permissions
from post.models import Post
from . import serializers
from .permissions import IsAuthorOrAdmin, IsAuthor


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':

            return serializers.PostListSerializer
        return serializers.PostCreateSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return serializers.PostCreateSerializer
        return serializers.PostDetailSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsAuthorOrAdmin

        elif self.request.method in ('PUT', 'PATCH'):
            return IsAuthor,

        return permissions.AllowAny(),
