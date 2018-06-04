# CS925

This repository contains all the programming assignments done for the course CS925 - Advanced Computer Networks during Spring 2017.

Language: Python

## Assignment 1
The goal of this assignment is to explore latency of a simple request/response interaction implemented using various of protocols and running over links with different latencies. The system consists of a client requesting a simple piece of information from a server, the server responds with the information, the client receives it, and measures, as precisely as possible, the time the entire transaction took.

Experiment with four protocols: raw data over UDP, raw data over TCP, HTTP, and HTTPS. To make it slightly more complicated, all protocols must run over IPv6. Both request and response should be few tens of bytes in length.

## Assignment 2
Write a simple discrete-event simulator of an M/M/1 queuing system with a bounded queue (such systems are referred to as M/M/1/k, where k is the size of the queue).

To test the simulator, design and run experiments to verify that simulation results are in line with known analytical results for the case where the queue is unbounded. It is sufficient to focus on just one measure, for example the mean waiting time. Experiment with finite-size queues and show the impact of different queue sizes on the performance measure studied in the first part.

The main goal of the assignment is to evaluate the correctness of simulated results by comparing them to theoretical results. The simulator itself is a tool but not the main outcome of the assignment. The design and execution of the experiments constitute a significant portion of the assignment. 

## Assignment 3
The goal is to build and verify functionality of a tool that will be used in a subsequent assignment. Write a simple program that measures the throughput of links between rb1 and rb2. 
The only requirements are:
- The data transmission must use TCP in the transport layer (raw TCP or HTTP would satisfy this requirement)
- The communication must have form of a request from client to what the server responds with a bulk data transfer for which you will measure throughput. HTTP GET is an example of such an exchange but you can come up with your own.
- You must be able to make the observation on both the client and the server side, i.e., how long it took for the client to get the data and how long it took the server to send it. For a large data transfer (1 MB is recommended), the two measurements will be very similar but you are still expected to measure and report both.

## Assignment 4
The goal of this assignment is to design, implement and verify an algorithm to estimate the download time of a media segment over a TCP connection. The algorithm must utilize observations made at both client and server side of the transfer. Such an algorithm could be used at the core of an adaptive bitrate streaming scheme.

The solution should repeatedly download a segment of approximately 1 MB and progressively improve the estimate of the download time. The exact arrangement is up to you and so is the way you evaluate the performance.

## Assignment 5
The goal of this assignment is to develop a method to measure one-way latency by taking advantage of precise time synchronization.

- First take advantage of a low latency, symmetric link to find out the offset between system clocks on rb1 and rb2. Note that in practice, you would not have such a link available and would have to resort to clock synchronization using other means, such as GPS.
- Second, design and implement a method to measure one-way latencies in each direction of the links that connect the interfaces. Since you know the offset between the system clocks of the two systems and plus that you can observe send time of a packet (measured using the clock on the sending system) together with the corresponding receive time (measured using the clock on the receiving system), obtaining one-way latency observation should be straightforward. All measurements are subject to random variations and so you are expected to come up with additional steps to improve the precision of your observations.
