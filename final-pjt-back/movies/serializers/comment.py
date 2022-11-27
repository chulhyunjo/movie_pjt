from rest_framework import serializers
from ..models import Comment, Movie
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields=('id',)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields=('id','username',)

    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'