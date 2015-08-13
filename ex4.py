cars=100
space_in_a_car=4.0
drivers=30
passengers=90
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpoll_capacity=cars_driven* space_in_a_car
average_passengers_per_car=passengers/cars_driven

print "there are",cars,"cars available."
print "there are only ",drivers,"drivers available"
print "there will be",cars_not_driven,"empty cars today"
print "we can transport",carpoll_capacity,"to carpool today."
print "We have",passengers,"to carpool today"
print "We have",average_passengers_per_car,"in each day."