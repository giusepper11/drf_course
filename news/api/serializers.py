from rest_framework import serializers
from news.models import Article
from datetime import datetime
from django.utils.timesince import timesince


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        # fields = "__all__"
        # fields = ("title", "description", "body", 'time_since_publication')
        exclude = ("id", "created_at", "updated_at")

    @staticmethod
    def get_time_since_publication(obj):
        publication_date = obj.publication_date
        now = datetime.now()
        return timesince(publication_date, now)

    def validate(self, data):
        """Checar se a descricao e o titulo sao diferentes"""
        if data['title'] == data['description']:
            raise serializers.ValidationError("Titulo e descricao devem ser diferentes um do outro")
        return data

    @staticmethod
    def validate_title(value):
        if len(value) < 60:
            raise serializers.ValidationError("Titulo precisa ter pelo menos 60 caracteres")

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def validate(self, data):
#         """Checar se a descricao e o titulo sao diferentes"""
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Titulo e descricao devem ser diferentes um do outro")
#         return data
#
#     @staticmethod
#     def validate_title(value):
#         if len(value) < 60:
#             raise serializers.ValidationError("Titulo precisa ter pelo menos 60 caracteres")
