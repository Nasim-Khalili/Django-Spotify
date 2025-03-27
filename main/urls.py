from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('view_playlist/<int:pk>/', views.view_playlist, name='view_playlist'),
    path('all_playlists/', views.all_playlists, name='all_playlists'),
]