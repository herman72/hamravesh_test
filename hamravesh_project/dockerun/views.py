from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from models import DockerApp


def create_docker(request):
    if request.method != "POST":
        return JsonResponse("", status=400)
    else:
        name = request.Post.get("name")

        DockerApp(name=name, )

    return HttpResponse


def get_app(request):
    return HttpResponse


def del_app(request):
    return HttpResponse


def edit_app(request):
    return HttpResponse
