from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag
from .forms import CommentForm
from django.contrib import messages

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Your comment was submitted successfully!")
            return redirect('blog:post_detail', slug=slug)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, is_published=True)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, is_published=True)
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})
