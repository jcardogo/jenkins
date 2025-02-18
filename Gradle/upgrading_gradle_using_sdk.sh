#This code is intended to run on UBUNTU linux servers
curl -s "https://get.sdkman.io" | bash #Installing sdk tool
source "/home/acardogo/.sdkman/bin/sdkman-init.sh" #initialising the sdktool
sdk help #Checking sdk funtions
sdk install gradle 8.12.1 #Upgrading gradle to specific version
gradle --version #CHecking upgrading result
