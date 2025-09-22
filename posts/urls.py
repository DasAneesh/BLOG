from posts import views
from django.urls import path
 


urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('login/' ,views.login, name='login'),
    path('about/' ,views.about, name='about'),
]