import sys
from cx_Freeze import setup, Executable

setup(
        name="WIFIPW",
        version="1.0",
        description = "WIFIPW",
        author = "edhz8888",
        executables = [Executable(script="wifipw.py")])