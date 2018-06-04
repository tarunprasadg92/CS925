The implementation needed for this assignment is done through the following files.
The name of the files, followed by a brief description about its purpose is
given below.

theoretical_curve.py
--------------------
This python file generates the theoretical values of the residency time for
different loads using the mathematical formula.

curve_1.py
----------
This file performs and computes the mean residency time for different loads in 
unbounded queueing system. The arrival time is computed using the inter-arrival
rate and the departure time is computed from the arrival time and the service 
times. Based on these two values, the mean residency time is computed.

curve_2.py
----------
This is the extension of the above file, except that implements a bounded queue
and thus all the timings are analysed and the queueing mechanism is followed.
Arrivals are enqueued and departures are dequeued. Beyond the queue size, the 
arrivals are dropped. Finally, we compute the mean residency time for the packets
that are not dropped.
