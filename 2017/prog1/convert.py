#!/usr/bin/python

"""
import pickle

testdata = [(1,2),(3,4)]
with open("test.pickle", "wb") as f:
	pickle.dump(testdata, f, 0)
"""

with open("abc.txt", "r") as infile:
	data = infile.read().split('),')

	print "len(data) = {}".format(len(data))
	print "data[0] = {}".format(data[0])
	print "data[1] = {}".format(data[1])

	data2 = [x.strip().strip('[').strip(']').strip('(').strip(')') for x in data]

	print "data2[0] = {}".format(data2[0])
	print "data2[1] = {}".format(data2[1])

	data3 = [x.split(',') for x in data2]

	print "data3[0] = {}".format(data3[0])
	print "data3[1] = {}".format(data3[1])

	data4 = [(int(x[0]),int(x[1]),int(x[2])) for x in data3]

	print "len(data4) = {}".format(len(data4))
	print "data4[0] = {}".format(data4[0])
	print "data4[1] = {}".format(data4[1])

	data5 = [x for x in data4 if x[0] != 255 or x[1] != 255 or x[2] !=255]

	print "len(data5) = {}".format(len(data5))
	print "data5[0] = {}".format(data5[0])
	print "data5[1] = {}".format(data5[1])

	with open("var.txt", "w") as outfile:
		for d in data5:
			outfile.write(str(d) + "\n")

"""
z = open('abc.txt','r+') 
m = mmap.mmap(z.fileno(), 0)

global a
a = int(m.read())
z.close()
end = time.clock()
secs = (end - start)
print("Number read in","%s" % (secs),"seconds.", file=f)
print("Number read in","%s" % (secs),"seconds.")
f.flush()
del end,start,secs,z,m
"""


from PIL import Image
from struct import pack

imgdata = b""
for d in data4:
    imgdata += pack("BBB", d[0], d[1], d[2])
im = Image.frombytes("RGB", (569,929), imgdata)
im.save("test.png", "PNG")
im2 = Image.frombytes("RGB", (929,569), imgdata)
im2.save("test2.png", "PNG")
