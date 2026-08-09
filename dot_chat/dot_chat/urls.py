"""
URL configuration for dot_chat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('request_page/',views.request_page,name='request_page'),
    path('register/',views.register_page,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('message/<int:receiver_id>/', views.message_page, name='message_page'),
    path('add_friend/<int:receiver_id>/', views.add_friend, name='add_friend'),
    path('delete_friend/<int:receiver_id>/', views.delete_friend, name='delete_friend'),
    path('cancel_friend_request/<int:receiver_id>/', views.cancel_friend_request, name='cancel_friend_request'),
    path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('friend_list/<int:user_id>/', views.friend_list, name='friend_list'),
    path('search_page/',views.search_page,name='search_page'),
    path('edit_page/<int:user_id>/', views.edit_page, name='edit_page'),
    path('edit_username/<int:user_id>/',views.edit_username,name='edit_username'),
    path('edit_email/<int:user_id>/',views.edit_email,name='edit_email'),
    path('edit_password/<int:user_id>/',views.edit_password,name='edit_password'),
    path('verify_password/<int:user_id>/',views.verify_password,name='verify_password'),
]
