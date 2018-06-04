import socket
import time
import requests

def run_experiment(protocol, interface):
	if protocol == "udp":
		udp_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
		udp_port = 8008
		
		udp_addr = (interface, udp_port)
		start = time.time()
		udp_socket.sendto(send_data, udp_addr)
		recv_data, server = udp_socket.recvfrom(1024)
		udp_socket.close()
		end = time.time()

		print ((end - start) * 1000)
		
	if protocol == "tcp":
		tcp_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
		tcp_port = 8009
		
		start = time.time()
		tcp_socket.connect((interface, tcp_port))
		tcp_socket.send(send_data)
		recv_data = tcp_socket.recv(1024)
		tcp_socket.close()
		end = time.time()
				
		print ((end - start) * 1000)
		
	if protocol == "http":
		address = "http://[" + interface + "]:8081/~tg1052/data.txt"
		start = time.time()
		r = requests.get(address)
		end = time.time()
		
		print ((end - start) * 1000)
		
	if protocol == "https":
		address = "https://[" + interface + "]:8443/~tg1052/data.txt"
		start = time.time()
		r = requests.get(address, verify=False)
		end = time.time()
		
		print ((end - start) * 1000)

send_data = "Hello RB2.."

protocols = ["udp", "tcp", "http", "https"]
interfaces = ["fd50:4abe:b885::2", "fd50:4abe:b885:1::2", "fd50:4abe:b885:2::2", "fd50:4abe:b885:3::2"]

for protocol in protocols:
	print "Protocol : ", protocol
	for interface in interfaces:
		print "Interface : ", interface
		print "Time taken for successive attempts (in ms) :"
		for try_count in range(0, 20):
			run_experiment(protocol, interface)
			
		print "\n"
