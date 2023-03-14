from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        children = instance.children.all()
        if children:
            repr['children'] = CategorySerializer(children, many=True).data

        return repr

