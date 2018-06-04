This assignment involves creating a client and server which uses a TCP connection
to transfer a large amount of data between them (around 1 MB in our case). The
implementation is done in Python and the function of each of the files present
is given below:

client_tcp.py
-------------
The client creates a socket and uses one of the 4 interfaces to connect to the
server. An arbitrary port number is used. The request is sent and the length of 
the response is received first. The client uses this information to decide how
long the connection must be kept open, as there is no way for the client to know
when the data transfer is complete. The total time taken for sending the request
and receiving the response is printed out.

server_tcp.py
-------------
The server creates a socket and keeps listening for request on the arbitrary
port number. Once the request arrives, the server starts sending the file to the 
client. The time taken for this is printed out.
