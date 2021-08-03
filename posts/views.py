from django.forms.utils import ErrorDict
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from posts.models import Post
from posts.forms import PostForm, SearchForm
from comments.forms import CommentForm
from posts.utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin



def posts_lists_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/index.html', context={'posts': posts})
    elif request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_param = search_form.cleaned_data['search_param']
            filtered_posts =  Post.objects.filter(title__icontains=search_param)
            return render(request, 'posts/index.html', context={'posts': filtered_posts})
def post_detail_view(request, id):
    post = get_object_or_404 (Post, id=id)
    return render(request, 'posts/post_detail.html', context={'post': post})

def news(request):
    news = Post.objects.all()
    return render(request, 'posts/index.html'), {'all_news': news}


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'posts/post_detail.html', context={'post': post, 'comments': comments, 'comment_form': comment_form})



class PostCreateView(View, ObjectCreateMixin):
    form = PostForm
    template = 'posts/post_create.html'


class PostUpdateView(View, ObjectUpdateMixin):
    bound_form = PostForm
    template = 'posts/post_update.html'
    obj_class = Post


class PostDeleteView(View, ObjectDeleteMixin):
    template = 'posts/post_delete.html'
    obj_class = Post
    redirect_template = 'posts_list_url'
    