from django.urls import path
from .views import GetListApp, CreateDocker, GetApp, DeleteApp, EditApp, RunApp, ListAppRuning


urlpatterns = [
    path("create/", CreateDocker.as_view(), name="create_dockerun"),
    path("list/", GetListApp.as_view(), name="get_list_dockerun"),
    path("get/", GetApp.as_view(), name="get_dockerun"),
    path("del/", DeleteApp.as_view(), name="del_dockerun"),
    path("edit/", EditApp.as_view(), name="edit_dockerun"),
    path("run_app/", RunApp.as_view(), name="runApp_dockerun"),
    path("list_run/", ListAppRuning.as_view(), name="list-app-running-dockerun"),
]
