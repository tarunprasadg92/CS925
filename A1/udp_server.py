import socket

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
server_socket.bind(('', 8008))
response = "Test data for UDP"

while True:
    message, address = server_socket.recvfrom(1024)
    server_socket.sendto(response, address)
