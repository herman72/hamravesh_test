import subprocess
from ast import literal_eval
from rest_framework.views import APIView
from .models import DockerApp, ExecutionApp
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import os
from subprocess import call
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt


class CreateDocker(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        app_detail = DockerApp()
        name = request.data["name"]
        image = request.data["image"]
        envs = request.data["envs"]
        command = request.data["command"]
        app_detail.name = name
        app_detail.image = image
        app_detail.envs = envs
        app_detail.command = command

        app_detail.save()

        return Response({"info": "all data saved"}, status=200)



class GetListApp(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all_apps = DockerApp.objects.all().values()
        list_app = []
        for i in range(len(all_apps)):
            list_app.append(all_apps[i])

        return Response({"list of app":list_app}, status=200)


class GetApp(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        name = request.data["name"]
        app = DockerApp.objects.filter(name=name).values()
        if len(app) == 0:
            return Response({"info": "there is no app with that name"})
        else:
            return Response({"app":app})


class DeleteApp(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        name = request.data["name"]
        app = DockerApp.objects.filter(name=name).values()
        if len(app) == 0:
            return Response({"info":"there is no app with that name"})
        else:
            app_delete = DockerApp.objects.filter(name=name)
            app_delete.delete()
            return Response({"info": app[0]["name"] + " deleted!"})



class EditApp(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        name = request.data["name"]
        app = DockerApp.objects.filter(name=name).values()
        if len(app) == 0:
            return Response({"info":"there is no app with that name"})
        else:
            list_of_edit = list(request.data.keys())
            app_edit = DockerApp.objects.get(name=name)
            for i in list_of_edit:
                app_edit.__dict__[str(i)] = request.data[str(i)]
            app_edit.save()

            return Response({"info": "all change data saved"}, status=200)


class RunApp(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data["name"]
        app = DockerApp.objects.filter(name=name).first()

        correct_values = app.envs.replace('[', '{')
        correct_values = correct_values.replace(']', '}')
        all_values = literal_eval(correct_values)
        all_keys = list(all_values.keys())
        variable_string = str()

        for i in range(len(all_values)):
            value = all_values[all_keys[i]]
            variable_string =variable_string+"-e "+str(all_keys[i])+"="+str(value)+" "

        run_docker = "docker run -d "+variable_string+"-l l1=v1 "+str(app[0]["image"])
        returned_output = subprocess.check_output(run_docker, shell=True)
        returned_output = (returned_output.decode("utf-8"))
        # exec_docker = "docker exec" + returned_output + +str(app[0]["command"])
        # subprocess.check_output(exec_docker, shell=True)

        # docker_app = DockerApp.objects.filter(name=name)

        exe_app = ExecutionApp()
        exe_app.app = app

        exe_app.run_params = app[0]["envs"]
        exe_app.is_running = True
        exe_app.created_container_id = returned_output
        exe_app.save()

        return Response({"info": "run the app"+name})

class ListAppRuning(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        exe_app = ExecutionApp.objects.all().values()
        return Response({"statues app":exe_app})