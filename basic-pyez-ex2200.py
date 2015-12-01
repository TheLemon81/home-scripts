#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.op.ethport import *
from jnpr.junos.factory import loadyaml
from pprint import pprint

#Loads the custom .yml file using the loadyaml function imported.  Manual way.
#mydefs = loadyaml('ethport.yml')
ospfNeighbors = loadyaml('yaml-definitions/ospfneighbors2.yml')
globals().update(ospfNeighbors)
 
ex2200 = Device(host='192.168.2.1',user='dlemon',password='w00ti3s')

eths = EthPortTable(ex2200)
ospfneighbors = OSPFNeighborTable(ex2200)

ex2200.open()


interface = "ge-0/0/0"


ospfneighbors.get()

# Example of if statements to determine certain things
print eths.get()
if  eths['ge-0/0/0'].oper == "up":
	print "ge-0/0/0 is up"
else:
	print "it's down"


print
print "ge-0/0/0 mtu"
print "############"
print

print eths[interface].mtu

#Assigns variable ae0 to all items in the table for ae0
ae0 = eths['ae0']

print
print "ae0 values"
print "##########"
print


print ae0.values()

print
print eths.items()
#print eths.values()
print
pprint(ospfneighbors)
print ospfneighbors.items()
print ospfneighbors.values()

 
ex2200.close()
