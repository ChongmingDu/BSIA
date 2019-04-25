# BSIA(Basic software initialization in ansible)

具体情况请根据自身需要选择模块。本环境已经在阿里云和腾讯云做过充足测试。如果在其他环境使用，请自行关闭selinux和防火墙。

## Base
Base模块主要初始化了新系统的一些参数（需要的包以及kernel调优参数）和中间件的安装。

### Base role内容
* openjdk 1.8
* docker 17.12.1-ce
* git 2.9.5

## Nginx
nginx模块初始化了nginx配置及基本的配置文件模版。

### Nginx role内容
* nginx 1.14.2

## Mongodb
Mongodb模块初始化了mongo基本配置。

### Mongodb role内容
* Mongodb 4.0

## Redis
Redis模块初始化了redis单点配置及基本的配置模版

### Redis role内容
* redis 5.0.3

## Zabbix_server and Zabbix_agent
Zabbix server role配置了zabbix server的基本配置(需要手动的配置参数)，和有关alertscripts的脚本模版。Zabbix agent role配置了zabbix agent的基本配置(需要手动配置参数)。

### Zabbix_server role内容
* zabbix server 4.0

### Zabbix_agent role内容
* zabbix agent 4.0

## Zookeeper
Zookeeper模块初始化了zk单点配置及基本的配置模版

### Zookeeper role内容
* zookeeper 3.4.9

* * *

## 使用
```
    1. 修改host.yml.examples中内容为远程主机公网地址，并重命名此文件为host.yml
    2. 修改roles/nginx/templates/examples.conf或roles/nginx/templates/examplesadmin.conf内容，把文中“examples”替换成需要的URL。其中，roles/nginx/templates/examples.conf适合前后分离的web环境。
    3. 如果使用zabbix role。请修改变量 roles/zabbix_server/templates/zabbix_server.conf（DB开头的三个变量），roles/zabbix_agent/templates/zabbix_agentd.conf（Server变量），roles/zabbix_server/files/zabbix_db.sh（mysql的变量），var/main.yml（mysql args变量）
    4. 运行 ansible-playbook -i host.yml  -u root standard.yml(默认全部role都开启)
    5. 如果使用zabbix role 请运行: ansible-playbook -i host.yml  -u root zabbix.yml
```