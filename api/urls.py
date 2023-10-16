from django.urls import path, include
from .import views
from api.views import postdetailview, postListView,PostView
from rest_framework.routers import DefaultRouter,SimpleRouter

router = DefaultRouter()
router.register('posts', PostView)

post_List_View = PostView.as_view({
    "GET": "list",
    "POST": "create"
})


urlpatterns = [
    path('posts/', include(router.urls)),

    # path('posts/', views.postListView.as_view()),
    # path('posts/<str:id>/', views.postdetailview.as_view()),
    path('generics/posts/', views.postListView.as_view()),
    path('generics/posts/<str:id>/', views.postdetailview.as_view()),
]