from django.urls import path
from .views import register,login_view,logout,profile,update_profile,\
    create_blog,my_blogs,update_blog,delete_blog,sending_email

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout,name='logout'),


    path('profile/',profile,name='profile'),
    path('create_blog/',create_blog,name='create_blog'),
    path('update_profile/',update_profile,name='update_profile'),
    path('update_blog/<int:id>/',update_blog,name='update_blog'),
    path('my_blogs/',my_blogs,name='my_blogs'),
    path('sending_email/',sending_email,name='sending_email'),
    path('delete_blog/<int:id>/',delete_blog,name='delete_blog')
]

