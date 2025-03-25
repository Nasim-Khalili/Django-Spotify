from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('register_user/',views.register_user,name='register_user'),
     path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]