from django.urls import path
from git . import views
urlpatterns = [
    path('todos/', views.todo_index_create),
]