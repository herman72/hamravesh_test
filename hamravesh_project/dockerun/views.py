from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from models import DockerApp


def create_docker(request):
    if request.method != "POST":
        return JsonResponse({""}, status=400)
    else:
        app_detail = DockerApp()
        name = request.Post.get("name")
        image = request.Post.get("image")
        envs = request.Post.get("evs")
        command = request.Post.get("command")

        app_detail.name = name
        app_detail.image = image
        app_detail.envs = envs
        app_detail.command = command

        app_detail.save()

        return JsonResponse({"info": "all data saved"}, status=200)


def get_list_app(request):
    all_apps = DockerApp.objects.all()
    list_app = []
    for i in range(len(all_apps)):
        list_app.append(all_apps[i])

    return HttpResponse(list_app)


def get_app(request):
    name = request.GET.get("name")
    app = DockerApp.objects.filter(name=name)

    return HttpResponse(app)


def del_app(request):
    return HttpResponse


def edit_app(request):
    return HttpResponse


def run_app(request):
    return HttpResponse
