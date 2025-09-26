from posts import views
from django.urls import path
 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    # path('login/' ,views.login, name='login'),
    path('about/' ,views.about, name='about'),
    path('create/' ,views.create, name='create'),
    path('posts/<int:post_id>', views.retrieve, name='retrieve'),
    path('posts/<int:post_id>/update', views.update, name='update'),

    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]