import subprocess
from time import sleep
import sys

cmd = 'python3 interactive_demo.py'
print(cmd)
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

print("Done")