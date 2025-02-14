#To check networking connectivity
ping 8.8.8.8 #testing connectivity to internet
ping 192.168.2.27 #Testing connectivity to local laptop
ip address show #To check ip address
ip a #Also check ip address
ip route #to show the connectivity route router (gateway) + interface (ens18) protocol dhcp + IP 
nmcli #To fetch details on network
nmcli device show ens18 #Fetching devices network details
sudo nmtui #TO manage network configuration
