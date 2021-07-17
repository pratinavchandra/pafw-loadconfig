#input
xml=input("Enter XML filename uploaded to Panorama: ")
dvcgrp_from=input("Enter Device group name to load from: ")
temp_from=input("Enter Template name to load from: ")
dvcgrp_to=input("Enter Device group name to load into: ")
temp_to=input("Enter Template name to load into: ")
#Generate commands
tag="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/tag to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/tag from "+xml
interface="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name=\'"+temp_from+"\']/config/devices/entry[@name='localhost.localdomain']/network/interface to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name=\'"+temp_to+"\']/config/devices/entry[@name='localhost.localdomain']/network/interface from "+xml
zone="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name=\'"+temp_from+"\']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/zone to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name=\'"+temp_to+"\']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/zone from "+xml
vrouter="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name=\'"+temp_from+"\']/config/devices/entry[@name='localhost.localdomain']/network/virtual-router to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name=\'"+temp_to+"\']/config/devices/entry[@name='localhost.localdomain']/network/virtual-router from "+xml
services="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/service to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/service from "+xml
servicegrp="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/service-group to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/service-group from "+xml
addressobj="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/address to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/address from "+xml
addressgrp="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/address-group to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/address-group from "+xml
natrules="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/pre-rulebase/nat/rules to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/pre-rulebase/nat/rules from "+xml
policy="load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_from+"\']/pre-rulebase/security to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name=\'"+dvcgrp_to+"\']/pre-rulebase/security from "+xml
#Output
print("TAG")
print("")
print(tag)
print("")
print("Interface")
print("")
print(interface)
print("")
print("Zones")
print("")
print(zone)
print("")
print("Virtual Router")
print("")
print(vrouter)
print("")
print("Services")
print("")
print(services)
print("")
print("Service Groups")
print("")
print(servicegrp)
print("")
print("Address Objects")
print("")
print(addressobj)
print("")
print("Address Groups")
print("")
print(addressgrp)
print("")
print("NAT Rules")
print("")
print(natrules)
print("")
print("Security Rules")
print("")
print(policy)