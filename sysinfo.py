import os
import socket
import getpass

def show_sysinfo():
    hostname = socket.gethostname()
    user = getpass.getuser()
    cwd = os.getcwd()

    print("\n=== System Information ===")
    print(f"Hostname: {hostname}")
    print(f"User: {user}")
    print(f"Current Directory: {cwd}")
