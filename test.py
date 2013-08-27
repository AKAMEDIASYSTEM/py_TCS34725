# TCS34725 sensor library test

import TCS34725 as tcs
import time

tcs = tcs.TCS34725()
tcs.begin()
print 'gain 1'
tcs.setGain(1)
print tcs.getRawData()

print 'gain 2'
tcs.setGain(2)
print tcs.getRawData()

print 'gain 3'
tcs.setGain(3)
print tcs.getRawData()

print 'gain 0'
tcs.setGain(0)
print tcs.getRawData()

print 'gain 4, this should not work'
tcs.setGain(4)
print tcs.getRawData()

print 'set integration time 0xFF'
tcs.setIntegrationTime(0xFF)

while True:
	print tcs.getRawData()
	time.sleep(1)