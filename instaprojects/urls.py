from django.urls import path
from.import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('create=project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>',views.deleteProject,name="delete-project"),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('like-project/<str:pk>', views.likeProject, name="like-project"),
    path('comment-project/<str:pk>', views.commentProject, name="comment-project"),
    path('show-comment/<str:pk>', views.ShowComment, name="show-comment"),
    ]
