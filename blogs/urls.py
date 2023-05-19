from django.urls import path
from . import views


urlpatterns = [
    path('api/forum/get/', views.getBlogs),
    path('api/forum/get/<int:pk>/', views.getSoloBlog),
    path('api/forum/post/', views.postBlog),
    path('api/forum/put/<int:pk>/', views.putBlog),
    path('api/forum/delete/<int:pk>/', views.deleteBlog),
    path('api/forum/comment/<int:pk>/', views.comment),
]