from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import DockerApp
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response



@csrf_exempt
def create_docker(request):
    if request.method != "POST":
        return JsonResponse({"request method": "Post"}, status=400)
    else:
        app_detail = DockerApp()
        name = request.POST.get("name")
        image = request.POST.get("image")
        envs = request.POST.get("envs")
        command = request.POST.get("command")
        app_detail.name = name
        app_detail.image = image
        app_detail.envs = envs
        app_detail.command = command

        app_detail.save()

        return JsonResponse({"info": "all data saved"}, status=200)


def get_list_app(request):
    all_apps = DockerApp.objects.all().values()
    list_app = []
    for i in range(len(all_apps)):
        list_app.append(all_apps[i])

    return HttpResponse(list_app)


def get_app(request):
    name = request.GET.get("name")
    app = DockerApp.objects.filter(name=name).values()
    if len(app) ==0:
        return HttpResponse("there is no app with that name")
    else:
        return HttpResponse(app)


def del_app(request):
    name = request.GET.get("name")
    app = DockerApp.objects.filter(name=name).values()
    if len(app) == 0:
        return HttpResponse("there is no app with that name")
    else:
        app_delete = DockerApp.objects.filter(name=name)
        app_delete.delete()
        return HttpResponse(app[0]["name"]+" deleted!")



def edit_app(request):
    name = request.GET.get("name")
    app = DockerApp.objects.filter(name=name).values()
    if len(app) == 0:
        return HttpResponse("there is no app with that name")
    else:
        # print(list(request.GET.keys()))
        list_of_edit = list(request.GET.keys())
        app_edit = DockerApp.objects.get(name=name)
        for i in list_of_edit:
            # print(request.GET.get(str(i)))
            app_edit.__dict__[str(i)] = request.GET.get(str(i))
            # print(app_edit.__dict__["name"])
        app_edit.save()

        return JsonResponse({"info": "all change data saved"}, status=200)


def run_app(request):
    return HttpResponse
