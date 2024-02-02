from django.urls import path

from . import views

app_name = "Blog"
urlpatterns = [
    path("", views.blog_list, name="blog"),
    path("blog/<int:blog_id>", views.blog_detail, name="blog_detail"),
    path("blog/<int:blog_id>/<int:comment_id>", views.blog_reply, name="blog_reply"),
    path("blog/a_propos", views.blog_a_propos, name="a_propos"),
]

handler400 = 'Blog.views.bad_request'
handler403 = 'Blog.views.permission_denied'
handler404 = 'Blog.views.page_not_found'
handler500 = 'Blog.views.server_error'
