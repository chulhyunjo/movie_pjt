from rest_framework import serializers
from ..models import Movie

class MovieBackgroundSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Movie
        fields = ('id','backdrop_path',)

class MovieViewsSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Movie
        fields = ('id','views',)

class MovieQuizSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Movie
        fields = ('id','title','backdrop_path',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class UserMovieList(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview')

        


