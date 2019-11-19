from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model
class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'user')

class UserSerializers(serializers.ModelSerializer):
    todo_set = TodoSerializers(many = True)     # 1: N 관계에 있는 아이들
    class Meta:
        model = get_user_model()
        fields = ('id','username','todo_set')
