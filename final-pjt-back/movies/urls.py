from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('genrelist/', views.genrelist, name='genrelist'),
    path('quizlist/', views.quizlist, name='quizlist'),
    path('movielist/', views.getMovieList, name='getMovieList'),
    path('Top20List/', views.getTop20List, name='getTop20List'),
    path('commentlist/', views.getCommentList, name='getCommentList'),
    path('getMovieDetail/<int:movie_pk>/', views.getMovieDetail, name='getMovieDetail'),
    path('comment/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('getGenreName/<str:username>/', views.getGenreName, name='getGenreName'),
    path('backdrop_path/', views.getBackdropPath, name='getBackdropPath'),
    path('recommend/<int:genre_id>/', views.recommend, name='recommend'),
    path('recommend/usermostlike/', views.userMostLike, name='userMostLike'),
    path('<int:movie_pk>/comments/<str:username>/', views.comment_create),
    path('recommend/grade/<str:username>/', views.recommendGrade, name='recommendGrade'),
    path('recommend/follow/<str:username>/', views.recommendFollow, name='recommendFollow'),
    path('search/<str:search>/', views.search, name='search'),
]
