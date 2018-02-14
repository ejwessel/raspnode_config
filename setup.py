import subprocess

subprocess.call("apt-get update", shell=True)
subprocess.call("apt-get upgrade -y", shell=True)
subprocess.call("apt-get install vim -y", shell=True)
subprocess.call("apt-get install tmux -y", shell=True)
subprocess.call("apt-get install ansible -y", shell=True)

