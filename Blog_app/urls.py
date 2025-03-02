"""
URL configuration for chaiman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login_view, name="login_view"),
    path("Home/", views.Home, name="Home"),
    path("logout/", views.Logout_view, name="logout_view"),
    path("<int:post_id>/view_post/", views.view_post, name="view_post"),
    path("<int:post_id>/edit_post/", views.edit_post, name="edit_post"),
    path("<int:post_id>/delete_post/", views.delete_post, name="delete_post"),
    path("<int:post_id>/add_post_comment/", views.add_comment, name="add_comment"),
    path("search_post/", views.search_post, name="search_post"),
    path("create_post/", views.create_post, name="create_post"),
    # path("tweet/register/", views.register, name="register"),
]
