from django.urls import path
from . views import*

urlpatterns = [
    path('', home, name = 'home'),

    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

    path('profile/<str:username>/', profile, name = 'profile'),
    path('profile/<str:username>/update/', profile_update, name = 'profile_update'),
    path('profile/<str:username>/delete/', profile_delete, name = 'profile_delete'),

]