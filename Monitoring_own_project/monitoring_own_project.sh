mkdir grafana
cd grafana
docker compose up -d 
docker ps | grep grafana #check runing container
#on a web browser we have access to grafana with defauld credentials admin/admin
#/home/acardogo/Documents/GitHub/DevOps/Monitoring_own_peoject/Grafana/docker-compose.yml #location on my laptop of the docker-compose
sudo docker-compose -f /home/acardogo/Documents/GitHub/DevOps/Monitoring_own_peoject/Grafana/docker-compose.yml up -d #to start grafana docker container
sudo docker ps | grep grafana # to check port of working grafana
#####PROMETHEUS
mkdir prometheus
cd prometheus

###Node_explorer
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.darwin-amd64.tar.gz
sudo tar xvfz node_exporter-1.8.2.darwin-amd64.tar.gz


