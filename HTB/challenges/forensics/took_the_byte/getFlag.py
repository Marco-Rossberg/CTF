#!/usr/bin/python

byteArray = []

file =  open('password', 'rb')
content = file.read(192)
for byte in content:
	byteArray.append(byte)

newByteArray = list(reversed(byteArray))

print(newByteArray)
