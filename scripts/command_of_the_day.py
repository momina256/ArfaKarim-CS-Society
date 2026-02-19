#!/usr/bin/python3 
# command of the day (Linux)
from subprocess import run, check_output
import random
# check the /bin folder 
commands = check_output(["ls", "/bin"])
commands = commands.decode("utf-8")
commands = commands.split("\n")
command = random.choice(commands)
print(command)
