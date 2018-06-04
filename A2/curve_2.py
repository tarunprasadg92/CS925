import random
import itertools

no_of_packets = 10000
queue_size = 50
arrival_rate = 0.05
service_rate = 1.0

while (arrival_rate <= 1.0):
    inter_arrival_time = [random.expovariate(arrival_rate) for i in range(no_of_packets)]
    service_times = [random.expovariate(service_rate) for i in range(no_of_packets)]

    arrival_time = []
    for i in range(no_of_packets):
        arrival_time.append(sum(itertools.islice(inter_arrival_time, i)))

    departure_time = []
    departure_time.append(service_times[0])
    curr_time = departure_time[0]

    for i in range(1, no_of_packets):
        curr_time = max(departure_time[i - 1], arrival_time[i])
        departure_time.append(curr_time + service_times[i])

    queue_length = 0
    dropped_packets = []
    arrival_index = 0
    departure_index = 0

    while (arrival_index < len(arrival_time)):
        if (arrival_time[arrival_index] < departure_time[departure_index]):
            #print "Event: Arrival \t\t Time: ", arrival_time[arrival_index]
            if (queue_length >= queue_size):
                #print "Dropping packet", arrival_index
                dropped_packets.append(arrival_index)
            queue_length += 1
            arrival_index += 1
        else:
            #print "Event: Departure \t Time: ", departure_time[departure_index]
            queue_length -= 1
            departure_index += 1
    while (departure_index < len(arrival_time)):
        #print "Event: Departure \t Time: ", departure_time[departure_index]
        queue_length -= 1
        departure_index += 1

    total_residency_time = 0
    for i in range(no_of_packets):
        if i in dropped_packets:
            continue
        else:
            total_residency_time += (departure_time[i] - arrival_time[i])
    #print "Average Residency Time:"
    print total_residency_time / (no_of_packets - len(dropped_packets))
    #print len(dropped_packets)

    arrival_rate += 0.05;
