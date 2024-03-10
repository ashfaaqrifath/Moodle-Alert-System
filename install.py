import subprocess
import importlib

packages = ["telebot", "requests", "beautifulsoup4", "plyer"]

for pkg in packages:
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call(["pip", "install", pkg])
    else:
        pass