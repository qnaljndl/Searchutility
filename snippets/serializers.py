from datetime import datetime
from rest_framework import serializers
from snippets.models import Snippet, Maps_Search_autocomplete
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos']


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # searches = serializers.PrimaryKeyRelatedField(many=True, queryset=Maps_Search_autocomplete.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']


class MapSearchSerializer(serializers.ModelSerializer):
    # search_owner = serializers.ReadOnlyField(source='search_owner.username')

    class Meta:
        model = Maps_Search_autocomplete
        fields = ['id', 'search_place', 'user_id', 'username']


# class MapSearchSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     search_place = serializers.DateTimeField(auto_now_add=True)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         # instance.language = validated_data.get('language', instance.language)
#         # instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

