from django.urls import path
from .views import blog, post_detail, add_post, edit_post, delete_post


name_app = blog

urlpatterns = [
    path('', blog, name='blog'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]
