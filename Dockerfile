docker run -d \
--name=ReadySet \
--publish=3306:3306 \
-e MYSQL_ROOT_PASSWORD=root@123 \
-e MYSQL_DATABASE=Readyset \
mysql
