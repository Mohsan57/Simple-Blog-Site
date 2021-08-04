from django.urls import path, re_path
from register import views
urlpatterns = [
    path('', views.index, name='home'),
    path('singup', views.Register_user, name='singup'),
    path('singin', views.login_user, name='singin'),
    path('registration/success/<slug:user_slug>',
         views.success_message, name='success_message'),
    path('registration/failed', views.failed_message, name='failed_message'),
    path('profile/<slug:user_slug>', views.user_detail, name='profile'),
    path('profile/<slug:user_slug>/new-blog',
         views.blog_post, name='new_blog'),
    path('blog/<slug:blog_slug>', views.blog, name='blog'),
    path('<slug:user_slug>/blogs', views.user_blogs,name="user_blogs"),
]
