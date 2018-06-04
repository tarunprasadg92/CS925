import random
import itertools

no_of_packets = 10000
arrival_rate = 0.05
service_rate = 1.0

while (arrival_rate <= 1.0):
    inter_arrival_time = [random.expovariate(arrival_rate) for i in range(no_of_packets)]
    service_times = [random.expovariate(service_rate) for i in range(no_of_packets)]
    '''
    print "Inter-arrival times:"
    print inter_arrival_time
    print "Service times:"
    print service_times
    '''
    arrival_time = []
    for i in range(no_of_packets):
        arrival_time.append(sum(itertools.islice(inter_arrival_time, i)))
    '''
    print "Arrival Times:"
    print arrival_time
    '''
    departure_time = []
    departure_time.append(service_times[0])
    curr_time = departure_time[0]

    for i in range(1, no_of_packets):
        curr_time = max(departure_time[i - 1], arrival_time[i])
        departure_time.append((curr_time + service_times[i]))
    '''
    print "Departure Times:"
    print departure_time
    '''
    total_residency_time = 0
    #print "Time spent by packets in the system:"
    for i in range(no_of_packets):
        #print (departure_time[i] - arrival_time[i])
        total_residency_time += departure_time[i] - arrival_time[i]
    '''
    print "Total Residency Time:"
    print total_residency_time
    '''
    #print "Average Residency Time:"
    print total_residency_time / no_of_packets

    arrival_rate += 0.05;
