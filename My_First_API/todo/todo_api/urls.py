from django.urls import path,include
# from django.conf.urls import url

from .views import (
    ToDoDetailApiView,
    ToDoListApiView,
)

urlpatterns = [
    path("api",ToDoListApiView.as_view()),
    path("api/<int:todo_id>/",ToDoDetailApiView.as_view()),    
]
