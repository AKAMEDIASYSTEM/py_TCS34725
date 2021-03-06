# TCS34725 sensor library test

import TCS34725 as tcs
import time

tcs = tcs.TCS34725()
tcs.begin()
print 'gain x1'
tcs.setGain(0)
print tcs.getRawData()

print 'gain x2'
tcs.setGain(1)
print tcs.getRawData()

print 'gain x16'
tcs.setGain(2)
print tcs.getRawData()

print 'gain x60'
tcs.setGain(3)
print tcs.getRawData()

print 'gain 4, this should not work'
tcs.setGain(4)
print tcs.getRawData()

print ' setting gain to x2'
tcs.setGain(1)

print 'set integration time 0xFF'
tcs.setIntegrationTime(0xFF)

# print 'set integration time 0xF6'
# tcs.setIntegrationTime(0xF6)

# print 'set integration time 0xEB'
# tcs.setIntegrationTime(0xEB)

# print 'set integration time 0xD5'
# tcs.setIntegrationTime(0xD5)

# print 'set integration time 0xC0'
# tcs.setIntegrationTime(0xC0)

# print 'set integration time 0x00'
# tcs.setIntegrationTime(0x00)

# print 'set integration time 0x14 (should break)'
# tcs.setIntegrationTime(0x14)

print 'setting interrupt to true'
tcs.setInterrupt(True)

print 'setting interrupt to False'
tcs.setInterrupt(False)

print 'getting status'
print tcs.getStatus()

while True:
	print tcs.getRGBData()
	time.sleep(1)
	# print tcs.calculateColorTemperature(r,g,b)