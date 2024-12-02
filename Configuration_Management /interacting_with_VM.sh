curl curl wttr.in #Test the chase url connection on a weather web page that print on command
sudo apt upgrade
sudo apt install git 
# git clone https://acardogo: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@github.com/jcardogo/DevOps.git #this command will clone my own devopsrepo
git clone https://github.com/blue-kale/hello #Clone the git 
cd hello
ls -l
./hello_cloud.py
sudo apt install puppet #install puppet on any debian server
gcloud init #sets up the authentication procedure between the virtual machine and Google Cloud
gcloud compute instances create --source-instance-template webserver-template ws1 ws2 ws3 ws4 ws5



sudo apt-get update #patch the os to the latest available set of programs
sudo apt-get install apt-transport-https ca-centificates gnupg curl #Install required certificates 
sudo apt install curl #before fetching any url I had to install curl
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg #bringing gpg from google url
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list #add the line to list
sudo apt-get update && sudo apt-get install google-cloud-cli #get installer for google cloud cli
sudo apt install google-cloud-cli #installing google cloud 
gcloud init #to start the gcloud service 
gcloud compute ssh vm1 #to connect to the VM


