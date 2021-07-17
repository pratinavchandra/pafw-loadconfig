# Palo Alto Firewalls - Load XML config CLI cheatsheet
Clone repository -
```text
git clone https://github.com/pratinavchandra/pafw-loadconfig.git
```
### Tags
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/tag to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/tag from <config-file.xml>
```
### Interfaces
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='<Template>']/config/devices/entry[@name='localhost.localdomain']/network/interface to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='<Template>']/config/devices/entry[@name='localhost.localdomain']/network/interface from <config-file.xml>
```
### Zones
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='<Template>']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/zone to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='<Template>']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/zone from <config-file.xml>
```
### Virtual Routers
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='<Template>']/config/devices/entry[@name='localhost.localdomain']/network/virtual-router to-xpath /config/devices/entry[@name='localhost.localdomain']/template/entry[@name='<Template>']/config/devices/entry[@name='localhost.localdomain']/network/virtual-router from <config-file.xml>
```
### Services
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/service to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/service from <config-file.xml>
```
### Service Groups
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/service-group to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/service-group from <config-file.xml>
```
### Address Objects
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/address to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/address from <config-file.xml>
```
### Address Groups
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/address-group to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/address-group from <config-file.xml>
```
### NAT Rules
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/pre-rulebase/nat/rules to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/pre-rulebase/nat/rules from <config-file.xml>
```
### Security Rules
```text
load config partial mode merge from-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/pre-rulebase/security to-xpath /config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='<Device-group>']/pre-rulebase/security from <config-file.xml>
```
