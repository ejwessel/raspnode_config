import subprocess

#Install ansible. Allows the running of the ansible script
subprocess.call("apt-get update", shell=True)
subprocess.call("apt-get upgrade -y", shell=True)
subprocess.call("apt-get install ansible -y", shell=True)

#Run the ansible commands to set up the node
