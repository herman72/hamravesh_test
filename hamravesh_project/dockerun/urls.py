from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_docker, name="create_dockerun"),
    path("list/", views.get_list_app, name="get_list_dockerun"),
    path("get/", views.get_app, name="get_dockerun"),
    path("del/", views.del_app, name="del_dockerun"),
    path("edit/", views.edit_app, name="edit_dockerun"),
    path("run_app/", views.create_docker, name="runApp_dockerun"),
]
