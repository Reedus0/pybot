import os
import paramiko

from logger import *

ssh = paramiko.SSHClient()

def init_ssh():
    ssh_host = os.getenv("RM_HOST")
    ssh_port = os.getenv("RM_PORT")
    ssh_user = os.getenv("RM_USER")
    ssh_password = os.getenv("RM_PASSWORD")
    
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)
    
    log("Initiated ssh!")

def ssh_do(command):
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.read().decode()