#!/bin/bash

# MySQL Backup and Restore
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"
MYSQL_HOST="your_host"
MYSQL_DB="your_database"

# Backup MySQL database
mysqldump -u $MYSQL_USER -p$MYSQL_PASSWORD -h $MYSQL_HOST $MYSQL_DB > backup.sql

# Restore MySQL database
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -h $MYSQL_HOST $MYSQL_DB < backup.sql

# Node.js Deployment
NODE_APP_DIR="/path/to/node/app"
NODE_APP_NAME="your_node_app"

# Stop existing Node.js application
pm2 stop $NODE_APP_NAME

# Pull latest changes from Git repository
git pull origin main

# Install dependencies
npm install

# Start Node.js application
pm2 start $NODE_APP_NAME