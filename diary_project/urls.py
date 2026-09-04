from django.contrib import admin
from django.urls import path

from diaryapp import views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'diary/',
        views.diary_list,
        name='diary_list'
    ),

    path(
        'diary/create/',
        views.create_entry,
        name='create_entry'
    ),

    path(
        'diary/<int:entry_id>/',
        views.diary_detail,
        name='diary_detail'
    ),

    path(
        'diary/<int:entry_id>/edit/',
        views.edit_entry,
        name='edit_entry'
    ),

    path(
        'diary/<int:entry_id>/delete/',
        views.delete_entry,
        name='delete_entry'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),
]