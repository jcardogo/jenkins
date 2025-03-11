#Create a ssh key pair
ssh-keygen -t rsa -b 4096 -C "jcardogo@gmail.com" -f ~/.ssh/jenkins_agent_key # Recommended: RSA, 4096 bits
#ssh-copy-id appends your public key to the ~/.ssh/authorized_keys file on the remote server.
ssh-copy-id acardogo@192.168.2.42
ssh-copy-id acardogo@192.168.2.44

