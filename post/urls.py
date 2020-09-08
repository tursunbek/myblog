from django.urls import path
from . import views

urlpatterns=[
    path('<slug:slug>', views.tag_detail, name='tag_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('', views.post_list, name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]