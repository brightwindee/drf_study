from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.photo_index, name='photo_index'),
    path('<int:id>/', views.photo_detail, name='photo_detail'),
    path('<int:id>/edit/', views.photo_edit, name='photo_edit'),
    path('new/', views.photo_post, name='photo_post'),
]