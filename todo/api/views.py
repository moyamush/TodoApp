from rest_framework import viewsets, generics, status
from todo.models import CustomGroup, Task, CustomUser
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupSerializer, TaskSerializer, UserSerializer, UserDisplaySerializer
from todo.api.permissions import IsAdminUserOrReadOnly
from django.http import Http404
from .mail import MailScheduler
from .task_list import TaskList

from .serializers import MyTokenObtainPairSerializer #追加
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

#追加
class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

MailSchedulerClass = MailScheduler()
task_list = TaskList()

class GroupViewSet(viewsets.ModelViewSet):
    queryset = CustomGroup.objects.all()
    serializer_class = GroupSerializer


class TaskCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user_pk = self.kwargs.get("user_pk")
        user = get_object_or_404(CustomUser, pk=user_pk)
        serializer.save(user=user)
        task_list.create_task(serializer.data, user)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def put(self, request, *args, **kwargs):
        task_list.edit_task(self.get_object(), request.user)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        task_list.delete_task(str(self.get_object().id))
        return self.destroy(request, *args, **kwargs)


class CurrentUserAPIView(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request):
        print("rest-framework-request: ", request)
        serializer = UserDisplaySerializer(request.user)
        self.get_task(request)
        return Response(serializer.data)
    
    def put(self, request, format=None):
        user = self.get_object(request.user.id)
        serializer = UserDisplaySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_task(self, request):
        serializer = UserDisplaySerializer(request.user)
        task = serializer.data['user_task']
        return task

# class CurrentUserAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     print(CustomUser.objects.all())
#     serializer_class = UserDisplaySerializer
#     permission_classes = [IsAdminUserOrReadOnly]


class UserCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserOrReadOnly]


