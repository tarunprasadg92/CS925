import socket
import struct
import time

# Create socket and keep listening for request
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind(('', 8010))
server_socket.listen(1)

# Copy data to be sent into variable
f = open("file.txt", "rb")
l = f.read()

while True:
    conn, addr = server_socket.accept()
    start = time.time()

    # Receive the request
    data = conn.recv(1024)
    l = struct.pack('>I', len(l)) + l

    # Send the response with the length of the data in the beginning
    conn.sendall(l)
    end = time.time()
    print "Time taken : ", ((end - start) * 1000)

f.close()
conn.close()
