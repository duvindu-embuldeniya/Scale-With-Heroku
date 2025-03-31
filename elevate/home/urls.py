from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('profile/<str:username>/', profile, name ='profile'),
    path('profile/delete/<int:pk>/', deleteProfile, name = 'delete-profile'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

    path('thought/create/', createThought, name = 'thought-create'),
    path('thoughts/<str:username>', myThoughts, name = 'thoughts-mine'),
    path('thought/update/<int:pk>/', updateThought, name = 'thought-update'),
    path('thought/delete/<int:pk>/', deleteThought, name = 'thought-delete'),


]