from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from .serializers import UserSerializer, UserDetailSerializer, UserSerializer2, UserDetailSerializer2
# Create your views here.


@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    if len(password) < 8:
        data= {
            'fail' : '비밀번호가 너무 짧습니다.'
        }
        return JsonResponse(data)
    elif not any(s in password for s in '!@#$%&^*'):
        data = {
            'fail' : '비밀번호는 특수문자를 포함해야 합니다.'
        }
        return JsonResponse(data)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):    
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserDetailSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_like_movie(request, movie_id, username):
    user = get_object_or_404(get_user_model(), username=username)
    movie = get_object_or_404(Movie, pk=movie_id)
    if user.like_movies.filter(pk=movie.pk).exists():
        user.like_movies.remove(movie.pk)
        liked = False
    else:
        user.like_movies.add(movie)
        liked = True
    context = {
        'liked': liked,
        'count': user.like_movies.count()
    }
    return JsonResponse(context)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.data.get('id')
    if person.pk != user:
        if person.followers.filter(pk=user).exists():
            person.followers.remove(user)
            followed = False
        else:
            person.followers.add(user)
            followed = True
        context = {
            'isFollowed': followed,
            'followers_count': person.followers.count(),
            'followings_count' : person.followings.count(),
        }
        return JsonResponse(context)
    else:
        return HttpResponse(status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserList(request):
    users = get_user_model().objects.all().order_by('-score')
    serializer = UserSerializer2(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserId(request, username):
    user = get_user_model().objects.get(username=username)
    serializer = UserDetailSerializer2(user)
    return Response(serializer.data)

@api_view(['GET'])
def getFollowers(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followers = user.followers.all()
    serializer = UserDetailSerializer2(followers,many=True)
    return Response(serializer.data)