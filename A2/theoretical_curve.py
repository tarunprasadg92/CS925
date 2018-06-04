mean_residency_time = 0

mu = 1.0
lamb = 0.0

while (lamb <= 1.0):
    mean_residency_time = 1 / (mu - lamb)
    #print "Mu: ", mu, "Lambda: ", lamb, "Mean Residency Time: ", mean_residency_time
    print lamb, ",", mean_residency_time
    lamb += 0.05
