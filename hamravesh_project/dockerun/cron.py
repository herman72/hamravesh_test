import docker
from .models import ExecutionApp
def my_scheduled_job():

  all_exe_app = ExecutionApp.objects.filter(is_running=True)
  client = docker.from_env()
  list_container = client.containers.list()

  list_running = []
  for i in range(len(list_container)):
    str_container_id = list_container[i].id
    str_container_id = str_container_id.replace('\n',"")
    list_running.append(str_container_id)

  for exe_app in all_exe_app:

    if exe_app.created_container_id.replace('\n',"") not in list_running:
      exe_app.is_running = False
      exe_app.save()



  return True