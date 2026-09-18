import subprocess

subprocess.Popen("echo one", shell=True)

subprocess.Popen(
    "echo two",
    shell=True,
)

subprocess.Popen(
    shell=True,
    args="echo three",
)
