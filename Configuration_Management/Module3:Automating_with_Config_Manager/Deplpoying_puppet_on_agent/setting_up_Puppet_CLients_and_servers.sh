######To be run on Puppet Agent
sudo puppet config --serction master set autosign true #this is the way to set aoutoding, but this is not recommended on real used machines

#this command configures Puppet to automatically sign the certificate request of added nodes
ssh webserver
sudo apt install puppet
sudo puppet config set server ubuntu.example.com
sudo puppet agent -v --test

#####To be run on Puppet Master 
nano /etc/puppet/code/environmets/production/manifests/site.pp #create the site.pp manifest file by entering editing mode. define the server node 


#####To be run on Puppet Agent  
sudo puppet agent -v --test

sudo systemctl enable puppet #thi will start puppet agent to start when machine reboots
sudo systemctl start puppet #this command starts for the firstime the puppet service 
sudo sysetemctl status puppet #This command show if the puppet service is runing fine on the agent machine

#read :http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/


