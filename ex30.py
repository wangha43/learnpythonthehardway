#-*-coding:utf-8-*-
people = 30
cars = 40
trucks = 15

if cars > people:
	print "车比人多"
elif cars < people:
	print "人比车多"
else:
	print "相等"

if trucks > cars:
	print "that is too many trucks"
elif trucks < cars:
	print "Maybe we could take the trucks"
else:
	print "we still can not decide"

if people > trucks:
	print "OK take trucks"
else:
	print "FINE,let's stay home then"
