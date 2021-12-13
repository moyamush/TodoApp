from rest_framework import serializers
from todo.models import CustomGroup, Task, CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #追加

#トークンを発行するためのクラス
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        return token


class TaskSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # group = GroupSerializer()
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"
        #exclude = ("user", )


class GroupSerializer(serializers.ModelSerializer):
    group_task = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = CustomGroup
        fields = "__all__"


class UserDisplaySerializer(serializers.ModelSerializer):
    user_task = TaskSerializer(many=True, read_only=True)
    user_group = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_task = TaskSerializer(many=True, read_only=True)
    # user_group = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = "__all__"
