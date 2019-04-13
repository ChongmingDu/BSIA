# BSIA(Basic software initialization in ansible)


本系统采用松耦合模块化配置，具体情况清根据自身需要选择模块。

## Base

### 使用
    1. 修改host.yml.examples中内容为远程主机公网地址，并重命名此文件为host.yml
    2. 修改roles/nginx/templates/examples.conf或roles/nginx/templates/examplesadmin.conf内容，把文中“examples”替换成需要的URL。其中，roles/nginx/templates/examples.conf适合前后分离的web环境。
    3. 运行 ansible-playbook -i host.yml  -u root standard.yml

### 本环境内容
    1. nginx(tenginx 2.2.2)
    2. openjdk(1.8)
    3. docker(17.12.1-ce)
    4. git(2.9.5)

## Zabbix

### 使用
    1. 修改变量 roles/zabbix_server/templates/zabbix_server.conf（DB开头的三个变量），roles/zabbix_agent/templates/zabbix_agentd.conf（Server变量），roles/zabbix_server/files/zabbix_db.sh（mysql的变量），var/main.yml（mysql args变量）
    2. 运行ansible-playbook -i host.yml  -u root zabbix.yml
