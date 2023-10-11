from django.urls import path
from .import views

urlpatterns = [
    path('user-profile/', views.userProfile, name='user-profile'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('singel-profile/<str:pk>', views.singleProfile,
         name='single-profile'),
    path('follow/<str:pk>', views.follow, name = 'follow'),
    path('unfollow/<str:pk>', views.unfollow, name='unfollow'),
    path('followers/<str:pk>', views.followers, name='followers'),
    path('following/<str:pk>', views.following, name='following'),
    ]