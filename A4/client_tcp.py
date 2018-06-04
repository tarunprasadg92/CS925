import socket
import time
import requests
import struct

# Function to receieve specified amount of data
# http://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
def recvall(socket, n):
    data = ''
    while len(data) < n:
        packet = socket.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

# Function to send request and receive response
def run_experiment(interface, try_count):
    # Create socket and define port number
    tcp_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    tcp_port = 8010

    # Start timer, connect to server and make request
    start = time.time()
    tcp_socket.connect((interface, tcp_port))
    tcp_socket.send(send_data)

    # Get length of data
    raw_length = recvall(tcp_socket, 4)
    if not raw_length:
        return None
    recv_length = struct.unpack('>I', raw_length)[0]

    # Get the entire response
    data = recvall(tcp_socket, recv_length)
    end = time.time()

    # Write the response into file
    filename = "recv_" + interface + str(try_count) + ".txt" 
    f = open(filename, "wb")
    f.write(data)
    f.close()
    tcp_socket.close()

    # Return the time taken
    return ((end - start) * 1000)

# Request message
send_data = "Send me the file..."

# Set of interfaces to use
interfaces = ["fd50:4abe:b885::2", "fd50:4abe:b885:1::2", "fd50:4abe:b885:2::2", "fd50:4abe:b885:3::2"]

# Iterate through each interface for 20 times
for interface in interfaces:
    print "Interface : ", interface

    new_estimate = 0.0
    actual_times = []
    estimated_times = []

    for try_count in range(0, 50):
        # print "Approximate estimated time : ", new_estimate
        time_taken = run_experiment(interface, try_count)
        # print "Actual time taken : ", time_taken
        actual_times.append(time_taken)
        new_estimate = sum(actual_times) / float(len(actual_times))
        estimated_times.append(new_estimate)
    
    print "Estimated Times : ", estimated_times
    print "Actual Times : ", actual_times
    print "\n"
