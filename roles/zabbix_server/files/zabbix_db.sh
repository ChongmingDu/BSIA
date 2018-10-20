#!/bin/bash
mysql -u root -p1q2w3e4r  -e "create database zabbix character set utf8 collate utf8_bin;"
mysql -u root -p1q2w3e4r -D zabbix -e "grant all privileges on zabbix.* to zabbix@localhost identified by '1q2w3e4r';"
zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -p1q2w3e4r zabbix