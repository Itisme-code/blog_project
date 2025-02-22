from django.urls import path
from .views import home,blog_detail,create_comment,like_view,dislike_view,subscribe_view,blogs,about,contact_us

urlpatterns = [
    path("home/",home,name='home'),
    path("blog_detail/<int:id>/",blog_detail,name='blog_detail'),
    path("create-comment/<int:blog_id>/",create_comment,name='create_comment'),
    path("like/<int:blog_id>/",like_view,name='like'),
    path("dislike/<int:blog_id>/",dislike_view,name='dislike'),
    path("subscribe/<int:profile_id>/",subscribe_view,name='subscribe'),
    path("blogs/",blogs,name='blogs-filter'),
    path("blogs/<int:category>/",blogs,name='blogs'),
    path("about/",about,name='about'),
    path("contact_us/",contact_us,name='contact_us'),
    ]
