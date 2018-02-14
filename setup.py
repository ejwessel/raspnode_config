import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--skip_ansible_install",
                        action = "store_false",
                        help = "allows skipping of ansible install")
parser.add_argument("-c", "--currency_type",
                        required = True,
                        help="bitcoin, ethereum, litecoin")
parser.add_argument("--smtp",
                        action = "store_true",
                        help = "if you have the smpt server, port, username, and password you can set up alerting")
args = parser.parse_args()

#Install ansible. Allows the running of the ansible script
if (args.skip_ansible_install):
  subprocess.call("apt-get update", shell=True)
  subprocess.call("apt-get upgrade -y", shell=True)
  subprocess.call("apt-get install ansible -y", shell=True)

#Run the ansible commands to set up the node

print args.currency_type
if (args.smtp is not None):
  print args.smtp
