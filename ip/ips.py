import ipaddress

#IP = '192.168.0.0'
#addr = ipaddress.ip_address(IP) #strict = False

IP = '192.168.0.0/4'

net = ipaddress.ip_network(IP) #strict = False

print(net)
