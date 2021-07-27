import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Client created successfully')

host = 'localhost'
port = 5434

message = 'Hello, server!'

try:
    print('Client: ' + message)
    s.sendto(message.encode(), (host, port))
    
    data, server = s.recvfrom(4096)
    data = data.decode()
    print(server)
    print(data)
finally:
    print('Client: Closing connection')
    s.close()
