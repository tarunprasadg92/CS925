The following file provides the list of files used in this assignment along with
a brief explanation of the purpose of each of the files.

client.py
---------
This python file acts performs all the required computations of the client. It 
iterates over the 4 protocols and 4 interfaces and produces a request to the
server. The requests are forwareded to the server through the corresponding port
numbers for each of the protocol.

tcp_server.py
-------------
This file acts as the tcp server. It binds itself to a socket and keeps listening
on the specified port number. When the client's request is received, the reply
is automatically sent back to the client.

udp_server.py
-------------
This file acts as the udp server. Similar to the tcp_server.py, it binds itself
to a socket, and keeps listening. It sends a response to the client once it
receives a request.
