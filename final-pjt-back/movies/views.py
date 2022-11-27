from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Movie, Genre, Comment
from .serializers.genre import GenreSerializer
from .serializers.movie import MovieBackgroundSerializer, MovieListSerializer, UserMovieList, MovieQuizSerializer, MovieViewsSerializer
from .serializers.comment import CommentSerializer, CommentListSerializer
# Create your views here.


@api_view(['GET','PUT'])
def getMovieDetail(request,movie_pk):
    if request.method=="GET":
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)
    elif request.method=="PUT":
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieViewsSerializer(movie, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def genrelist(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def quizlist(request):
    quiz = Movie.objects.exclude(backdrop_path__isnull=True)
    quiz = quiz.order_by('?')[:4]
    serializer = MovieQuizSerializer(quiz, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBackdropPath(request):
    backdropPath = get_list_or_404(Movie)
    serializer = MovieBackgroundSerializer(backdropPath, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCommentList(request):
    comments = Comment.objects.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMovieList(request):
    movie = get_list_or_404(Movie)
    serializer = UserMovieList(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTop20List(request):
    movie = Movie.objects.all().order_by('-popularity')[:20]
    serializer = MovieListSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGenreName(request, username):
    now_user = get_object_or_404(get_user_model(), username=username)
    user_genre = []
    for genre_id in now_user.like_genres.all():
        user_genre.append(genre_id.id)
    genre1 = Genre.objects.filter(id__in=user_genre)
    serializer = GenreSerializer(genre1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommend(request, genre_id):
    movies = Movie.objects.all().order_by('?')[:500]
    movieList = []
    count = 0
    for movie in movies:
        if count == 10: break
        for genre in movie.genres.all():
            if genre.id == genre_id:
                count += 1
                movieList.append(movie.id)
                break

    movies = Movie.objects.filter(id__in=movieList)[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userMostLike(request):
    movies = Movie.objects.all()
    likeMovies = sorted(movies, key=lambda x: -x.users.count())[:10]
    serializer = MovieListSerializer(likeMovies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk, username):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), username=username)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    review = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'review {comment_pk} is deleted'
        }
    return Response(data)

@api_view(['GET']) # 좋아요 목록 장르 + 평점 order
@permission_classes([IsAuthenticated])
def recommendGrade(request, username):
    users = User.objects.exclude(username=username)
    user = get_object_or_404(get_user_model(), username=username)
    same_grade1, same_grade2, same_grade3 = [], [], []
    movie_point = {}
    # 동일 등급 유저가 좋아한 영화 id 조회
    for i in users.all():
        if i.score <= 30:
            same_grade1 += i.like_movies.all()
        elif i.score <= 70:
            same_grade2 += i.like_movies.all()
        else:
            same_grade3 += i.like_movies.all()
    if user.score <=30 :
        same_grade = same_grade1
    elif user.score <= 70:
        same_grade = same_grade2
    else:
        same_grade = same_grade3
    # 좋아요 점수 50점/ 조회수 점수 1점
    for movie in same_grade:
        try:
            movie_point[movie.id] += 20
        except:
            movie_point[movie.id] = 20
    
    movies_id=[]
    for movie in movie_point.keys():
        movies_id.append(movie)
        this_movie = Movie.objects.get(pk=movie)
        movie_point[movie] += this_movie.views
    
    movies = Movie.objects.filter(id__in=movies_id)
    movies = sorted(movies, key= lambda x: -movie_point[x.id])[:10]
    movie_point = sorted(movie_point.items(), key = lambda x : -x[1])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendFollow(request, username):
    now_user = User.objects.get(username=username)
    follow = now_user.followings.all()

    movie_obj = {}
    for i in follow:
        follow_movie = i.like_movies.all()
        for movie in follow_movie:
            try:
                movie_obj[movie.id] += 1
            except:
                movie_obj[movie.id] = 1

    movies_id=[]
    for movie in movie_obj.keys():
        movies_id.append(movie)

    movies = Movie.objects.filter(id__in=movies_id)
    movies = sorted(movies, key= lambda x: -movie_obj[x.id])[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search(request, search):
    search_movies = Movie.objects.filter(title__contains=search)
    search_movie = sorted(search_movies, key=lambda x: -x.popularity)[:10]
    serializer = MovieListSerializer(search_movie, many=True)
    return Response(serializer.data)
