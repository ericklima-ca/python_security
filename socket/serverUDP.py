import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created successfully')

host = 'localhost'
port = 5434

s.bind((host, port))

message = '\nServer: Hello, client!'

while True:
    data, addr = s.recvfrom(4096)

    if data:
        print('Server sending message')
        print(addr)
        print(data)
        s.sendto((message.encode()), addr)
        break
