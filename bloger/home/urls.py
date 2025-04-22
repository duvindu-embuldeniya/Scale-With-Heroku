from django.urls import path
from . views import*

urlpatterns = [
    path('', home, name = 'home'),

    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

    path('profile/<str:username>/', profile, name = 'profile'),
    path('profile/update/<str:username>/', profile_update, name = 'profile_update'),
    path('profile/delete/<str:username>/', profile_delete, name = 'profile_delete'),

    path('blog_detail/<int:pk>/', blog_detail, name = 'blog_detail'),
    path('author/<str:username>/', blog_author, name = 'blog_author'),
    path('blog_create/', blog_create, name = 'blog_create'),
    path('blog_update/<int:pk>/', blog_update, name = 'blog_update'),
    path('blog_delete/<int:pk>/', blog_delete, name = 'blog_delete'),
]