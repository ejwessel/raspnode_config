import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--skip-ansible-install",
                        action = "store_false",
                        help = "allows skipping of ansible install")
parser.add_argument("-c", "--currency-type",
                        required = True,
                        help="bitcoin, ethereum, litecoin")
parser.add_argument("--smtp",
                        action = "store_true",
                        help = "if you have the smpt server, port, username, and password you can set up alerting")
parser.add_argument("-d", "--dry-run",
                       action = "store_true",
                       help = "dry-run ansible playbook")
args = parser.parse_args()

#Install ansible. Allows the running of the ansible script
if (args.skip_ansible_install):
  subprocess.call("apt-get update", shell=True)
  subprocess.call("apt-get upgrade -y", shell=True)
  subprocess.call("apt-get install ansible -y", shell=True)

#Run the ansible commands to set up the node
dry_run = "--check" if (args.dry_run) else ""

command = 'ansible-playbook -v -i "localhost," --connection local playbook.yml %s --extra-vars "currency_type=%s setup_smtp=%s"' % (dry_run, args.currency_type, str(args.smtp))
print command
subprocess.call(command, shell=True)
