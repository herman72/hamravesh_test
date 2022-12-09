from django.contrib import admin
from django.urls import path
from . import views
from .views import GetListApp, CreateDocker, GetApp, DeleteApp, EditApp
urlpatterns = [
    path("create/", CreateDocker.as_view(), name="create_dockerun"),
    path("list/", GetListApp.as_view(), name="get_list_dockerun"),
    path("get/", GetApp.as_view(), name="get_dockerun"),
    path("del/", DeleteApp.as_view(), name="del_dockerun"),
    path("edit/", EditApp.as_view(), name="edit_dockerun"),
    path("run_app/", views.run_app, name="runApp_dockerun"),
]
