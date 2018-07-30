from django.shortcuts import render, redirect
from .models import Post

def profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/account/logout')
        return render(request, 'Features/profile.html')
    else:
        return redirect('/account/login')

def category(request, category):
    available_categories = ['programming','web-development','video-games','yourcategory']
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/account/logout')
        posts = Post.objects.all()
        for available_category in available_categories:
            if category == available_category:
                return render(request, 'Features/category.html', {'posts':posts,'category':category})
    else:
        return redirect('/account/login')

def newpost(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/account/logout')
        if request.method == 'POST':
            success = 'post saved successfully!'
            post_title = request.POST['title']
            post_body = request.POST['body']
            post_category = request.POST['category']
            post_author = request.user
            new_post = Post()
            new_post.author,new_post.title, new_post.body, new_post.category = post_author,post_title,post_body,post_category
            new_post.save()
            return render(request, 'Features/newpost.html', {'success':success})
        else:
            return render(request, 'Features/newpost.html')
    else:
        return redirect('/account/login')

def view_post(request, category, posttitle):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/account/logout')
        for post in Post.objects.all():
            if post.category == category and post.title == posttitle:
                return render(request, 'Features/view_post.html', {'post':post})
    else:
        return redirect('/account/login')