from django.shortcuts import render, redirect
from .models import Blog, Comment
from .forms import CommentForm


def blog_list(request):
    return render(request, 'Blog/index.html', {
        "blogs": Blog.objects.filter(visible=True).order_by("-date"),
        "unpublished_blogs": Blog.objects.filter(visible=False).order_by("-date"),
        "user": request.user,
        "title": "Lab'info"
    })


def blog_detail(request, blog_id):
    blog_choosed = Blog.objects.get(id=blog_id)
    comments = blog_choosed.comments.filter(parent=None).order_by("-date")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = None
            comment.blog = blog_choosed
            comment.save()
            return redirect('Blog:blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'Blog/blog.html', {
        "blog": blog_choosed,
        "comments": comments,
        "form": form,
        "title": blog_choosed.title
    })


def blog_reply(request, blog_id, comment_id):
    blog_choosed = Blog.objects.get(id=blog_id)
    comments = blog_choosed.comments.all().order_by("-date")
    comment_choosed = comments.get(id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = comment_choosed
            comment.blog = blog_choosed
            comment.save()
            return redirect('Blog:blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'Blog/blog.html', {
        "blog": blog_choosed,
        "comments": comments,
        "form": form,
        "title": blog_choosed.title
    })


def blog_a_propos(request):
    return render(request, 'Blog/a_propos.html', {
        "blogs": Blog.objects.all(),
        "comments": Comment.objects.all(),
        "title": "A propos"
    })


def bad_request(request, exception):
    return render(request, 'Blog/error.html', {
        "error": "400 Bad Request",
        "message": "Your browser sent a request that this server could not "
                   "understand."
    })


def permission_denied(request, exception):
    return render(request, 'Blog/error.html', {
        "error": "403 Forbidden",
        "message": "You don't have permission to access the requested resource."
    })


def page_not_found(request, exception):
    return render(request, 'Blog/error.html', {
        "error": "404 Not Found",
        "message": "The requested resource was not found on this server."
    })


def server_error(request):
    return render(request, 'Blog/error.html', {
        "error": "500 Internal Server Error",
        "message": "The server encountered an internal error and was unable "
                   "to complete your request."
    })
