from rest_framework import serializers
from snippets.models import Snippet



class SnippetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    dep = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)


    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance