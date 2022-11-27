from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('mypage/<str:username>/', views.profile, name='profile'),
    path('like/<str:username>/<int:movie_id>/', views.user_like_movie),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('getUserList/', views.getUserList, name='getUserList'),
    path('getUserId/<str:username>/', views.getUserId, name='getUserId'),
    path('getFollowers/<str:username>/', views.getFollowers, name='getFollowers'),

]