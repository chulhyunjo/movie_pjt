from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta : 
        model = get_user_model()
        fields = ('id','username', 'password', 'like_genres','score',)


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta : 
        model = get_user_model()
        fields = '__all__'

class UserDetailSerializer2(serializers.ModelSerializer):
    
    class Meta : 
        model = get_user_model()
        fields = ('id','username',)

class UserSerializer2(serializers.ModelSerializer):
    
    class Meta : 
        model = get_user_model()
        fields = ('id', 'username', 'followings', 'like_movies','score',)

# class UserFollowersSerializer2(serializers.ModelSerializer):
    
#     class Meta : 
#         model = get_user_model()
#         fields = '__all__'