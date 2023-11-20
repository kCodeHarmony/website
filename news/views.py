from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Post, Comment
import logging
from django.http import HttpResponse
# Create your views here.

db_logger = logging.getLogger('db')

def home(request):
    post = Post.objects.first()
    posts = Post.objects.all()[0:3]
    categories = Category.objects.all()[0:3]

    return render(request, 'home.html', {
        "post": post,
        "posts": posts,
        "categories": categories
    })


def posts(request):
    news = Post.objects.all()


    return render(request, 'news.html', {
        "news": news
    })


def categories(request):
    categories = Category.objects.all()

    return render(request, 'category.html', {
        'categories': categories
    })


def category(request, id):
    category = Category.objects.get(id=id)
    news = Post.objects.filter(category=category)

    return render(request, 'news-by-category.html', {
        "news": news,
        "category": category
    })


def post_details(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['message']
        email = request.POST['email']
        Comment.objects.create(
            post=post,
            title=name,
            email=email,
            content=comment
        )
        messages.success(request, 'Your comment now in moderation mode.')
    category = Category.objects.get(id=post.category.id)
    comments = Comment.objects.filter(post=post, status=True).order_by('-id')
    related_news = Post.objects.filter(category=category).exclude(id=id)


    return render(request, 'detail.html', {
        'news': post,
        'comments': comments,
        'related_news': related_news
    })
