from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path('', PostListView.as_view(), name='base'),
    path('blog/', PostListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/post_detail/', PostDetailView.as_view(), name='post_detail'),
    path('blog/add_post/', PostCreateView.as_view(), name='add_post'),
    path('blog/<int:pk>/edit_post/', PostUpdateView.as_view(), name='edit_post'),
    path('blog/<int:pk>/delete_post/', PostDeleteView.as_view(), name='delete_post'),
]
