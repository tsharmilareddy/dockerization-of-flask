from flask import Flask
import platform
import os
import getpass

app = Flask(__name__)

@app.route("/")
def get_system_info():
    os_name = platform.system()
    if os_name == 'Windows':
        os_version = platform.version()
    else:
        os_version = os.popen('cat /etc/os-release | grep "PRETTY_NAME="').readline().strip()

    home_dir = os.getenv('USERPROFILE')  # use USERPROFILE on Windows
    username = getpass.getuser()

    return f"Operating system: {os_version}<br>" \
           f"Home directory: {home_dir}<br>" \
           f"Current username: {username}"

if __name__ == '__main__':
    app.run()
