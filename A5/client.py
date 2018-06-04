import socket
import time
import requests

def run_experiment(interface):
	udp_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
	udp_port = 8008
		
	udp_addr = (interface, udp_port)
	print '%f' % (time.time() * 1000)
	udp_socket.sendto(send_data, udp_addr)
	recv_data, server = udp_socket.recvfrom(1024)
	udp_socket.close()
        print '%f' % (time.time() * 1000)
		
send_data = "Hello RB2.."

# initial_interface = ["fd50:4abe:b885:4::2"]
interfaces = ["fd50:4abe:b885::2", "fd50:4abe:b885:1::2", "fd50:4abe:b885:2::2", "fd50:4abe:b885:3::2"]

for interface in interfaces:
#for interface in initial_interface:
	print "Interface : ", interface
	print "Time taken for successive attempts (in ms) :"
	for try_count in range(0, 1):
		run_experiment(interface)
		
	print "\n"
