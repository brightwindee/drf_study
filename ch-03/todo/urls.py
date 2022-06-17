from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('<int:id>/edit/', views.todo_edit, name='todo_edit'),
    path('<int:id>/done/', views.todo_done, name='todo_done'),
    path('new/', views.todo_post, name='todo_post'),
    path('done/', views.done_list, name='done_list'),
]