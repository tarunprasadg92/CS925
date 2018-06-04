import socket

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind(('', 8009))
server_socket.listen(1)

response = "Test data for TCP"


while True:
    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    if not data:
        break
    conn.send(response)

conn.close()
