sudo /etc/init.d/mysql restart
mysql -uroot -p0 -e "create database myproject;"
mysql -uroot -p0 -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -p0 -e "GRANT ALL PRIVILEGES ON * . * TO 'enth'@'localhost';"
mysql -uroot -p0 -e "FLUSH PRIVILEGES;"
