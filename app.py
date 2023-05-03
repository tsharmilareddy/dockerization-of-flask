import platform
import os
import getpass

os_name = platform.system()
if os_name == 'Windows':
    os_version = platform.version()
else:
    os_version = os.popen('cat /etc/os-release | grep "PRETTY_NAME="').readline().strip()

home_dir = os.environ['HOME']
username = getpass.getuser()
print(f"Operating system: {os_version}")
print(f"Home directory: {home_dir}")
print(f"Current username: {username}")




