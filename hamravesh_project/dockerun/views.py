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

        return JsonResponse({""}, status=200)


def get_list_app(request):
    return HttpResponse


def get_app(request):
    return HttpResponse


def del_app(request):
    return HttpResponse


def edit_app(request):
    return HttpResponse


def run_app(request):
    return HttpResponse
