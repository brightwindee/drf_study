from django.urls import path
from .views import HelloAPIView, TodosAPIView, TodoAPIView, DoneTodosAPIView, DoneTodoAPIView

urlpatterns = [
    # /todo/, get/post
    path('', TodosAPIView.as_view()),
    # /todo/<id>/, get/put
    path('<int:id>/', TodoAPIView.as_view()),
    # /todo/done/
    path('done/', DoneTodosAPIView.as_view()),
    # /todo/done/<id>
    path('done/<int:id>', DoneTodoAPIView.as_view()),
]
