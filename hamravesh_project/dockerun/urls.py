from django.contrib import admin
from django.urls import path
from . import views
from .views import GetListApp, CreateDocker
urlpatterns = [
    path("create/", CreateDocker.as_view(), name="create_dockerun"),
    path("list/", GetListApp.as_view(), name="get_list_dockerun"),
    path("get/", views.get_app, name="get_dockerun"),
    path("del/", views.del_app, name="del_dockerun"),
    path("edit/", views.edit_app, name="edit_dockerun"),
    path("run_app/", views.run_app, name="runApp_dockerun"),
]
