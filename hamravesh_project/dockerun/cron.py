from .models import ExecutionApp
import subprocess
import docker
def my_scheduled_job():
  exe_app = ExecutionApp()
  all_exe_app = ExecutionApp.object.all()
  client = docker.from_env()
  list_container = client.containers.list()

  list_running = []
  for i in range(len(list_container)):
    list_running.append(list_container[i].id)

  for i in range(len(all_exe_app)):

    if all_exe_app[i]["created_container_id"] not in list_running:
      all_exe_app[i]["is_running"] = False
      # ExecutionApp.object.filter(created_container_id=)



  # returned_output = subprocess.check_output("docker ps", shell=True)

  return