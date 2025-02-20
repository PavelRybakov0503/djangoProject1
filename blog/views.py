from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3  # Количество постов на странице
    ordering = ['-created_at']  # Сортировка постов по дате создания в обратном порядке

    def get_queryset(self):  # фильтрация постов по опубликованным
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):  # увеличение счетчика просмотров
        post = super().get_object()
        post.views_count += 1
        post.save()
        return post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    fields = ['title', 'content', 'preview']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:base')

    def form_valid(self, form):  # изменение флага опубликованости при сохранении
        post = form.save(commit=True)
        post.published = True
        post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_detail')

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy('blog:post_detail', kwargs={'pk': post.pk})

    def form_valid(self, form):
        post = form.save(commit=True)
        post.published = True
        post.save()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy('blog:home')
    context_object_name = 'post'
