#!/usr/bin/python

for n in range(1,1000):
	res = 528601 / n
	mul = res * n
	if mul == 528601:
		print "528601 / {} = {}".format(n, 528601 / n)
