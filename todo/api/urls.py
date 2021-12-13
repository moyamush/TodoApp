from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (GroupViewSet, TaskCreateAPIView, TaskDetailAPIView,
                    UserCreateAPIView, UserDetailAPIView, CurrentUserAPIView)

router = DefaultRouter()

# api/todo/
router.register(r"group", GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path('users/', UserCreateAPIView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name="user-detail"),
    path('users/<int:user_pk>/task/',TaskCreateAPIView.as_view(), name="user-list"),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name="task-detail"),
    path('tasks/', TaskCreateAPIView.as_view(), name="task-list"),

    #追加
    #api/authアプリケーションのURLconf読み込み
    path('api/jwt/auth/', include('djoser.urls.jwt')),
]
