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

new_estimate = 0.0
actual_times = []
estimated_times = []

while True:
    conn, addr = server_socket.accept()
    start = time.time()

    # Receive the request
    data = conn.recv(1024)
    l = struct.pack('>I', len(l)) + l

    # Send the response with the length of the data in the beginning
    conn.sendall(l)
    end = time.time()
    time_taken = ((end - start) * 1000)
    actual_times.append(time_taken)
    new_estimate = sum(actual_times) / float(len(actual_times))
    estimated_times.append(new_estimate)

    if len(actual_times) == 50:
        print "Estimated timings : ", estimated_times
        print "Actual timings : ", actual_times
        print "\n"

        actual_times = []
        estimated_times = []
        new_estimate = 0.0

    f = open("file.txt", "rb")
    l = f.read()

f.close()
conn.close()
