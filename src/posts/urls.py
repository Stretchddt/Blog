from django.urls import path
from .views import all_posts_view, post_detail, post_update, post_delete, post_create

app_name = 'posts'

urlpatterns =[
    path('all/', all_posts_view, name='all-posts'),
    path('create/', post_create, name='create-post'),
    path('post/<str:pk>/', post_detail, name='detail-post'),
    path('post/update/<str:pk>/', post_update, name='update-post'),
    path('post/delete/<str:pk>/', post_delete, name='delete-post'),
]  