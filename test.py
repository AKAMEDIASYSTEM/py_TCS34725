# TCS34725 sensor library test

import TCS34725 as tcs
import time

tcs = tcs.TCS34725()
tcs.begin()
while True:
	print tcs.getRawData()
	time.sleep(1)