from django.shortcuts import render
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializers
# Create your views here.

#GET / todos/ : 전체 todos
# POST / todos : todos 등록

@api_view(['GET','POST'])
def todo_index_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializers = TodoSerializers(todos, many=True) 
        return Response(serializers.data)
    else:
        # request.POST : Form Data로 post 전송 되었을때
        # request.data : formData로 POST 전송 및 DATAㄹ 전송 모두
        serializers = TodoSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)

@api_view(['GET'])
def todo_delete_all(request):
    todos = Todo.objects.all()
    for todo in todos:
        todo.delete()
    
    return Response('clear!')