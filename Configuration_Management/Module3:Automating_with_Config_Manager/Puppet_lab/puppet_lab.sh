sudo apt install puppet-master
#(...)
#Processing triggers for systemd (240-6ubuntu5.7) ...
#Processing triggers for man-db (2.8.5-2) ...
#Processing triggers for fontconfig (2.13.1-2ubuntu2) ...
vim tools.pp
htop
#-bash: /usr/bin/htop: No such file or directory
sudo puppet apply -v tools.pp
#Info: Loading facts
#Notice: Compiled catalog for ubuntu in environment production in 0.02 seconds
#Info: Applying configuration version '1572272642'
#Notice: /Stage[main]/Main/Package[htop]/ensure: created
#Notice: Applied catalog in 3.81 seconds
htop
sudo puppet apply -v tools.pp
#nfo: Loading facts
#Notice: Compiled catalog for ubuntu in environment production in 0.02 seconds
#Info: Applying configuration version '1572281655'
#Notice: Applied catalog in 0.07 seconds

sudo puppet apply -v ntp.pp
