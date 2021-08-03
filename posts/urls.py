from django.urls import path
from posts.views import PostDeleteView, posts_lists_view, post_detail, PostCreateView, PostUpdateView

urlpatterns = [
    path('', posts_lists_view, name='posts_list_url'),
    path('<int:id>/', post_detail, name='post_detail_url'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update_url'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete_url'),
]

