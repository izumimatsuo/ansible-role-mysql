# ansible-role-mysql [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-mysql.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-mysql)

CentOS 7 に mysql を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名                  |デフォルト値|説明
------------------------|------------|----------
mysql_listen_port       |3306        |ポート番号
mysql_admin_password    |None        |管理者パスワード
mysql_replication       |no          |レプリケーション要否(yes/no)

レプリケーション要否が yes の場合は以下も設定する。

項目名                         |説明
-------------------------------|----------
mysql_replication_user.name    |レプリケーション用ユーザ名
mysql_replication_user.password|レプリケーション用ユーザパスワード
mysql_replication_master       |マスターホストのホスト名かアドレス
mysql_server_id                |ホストID
mysql_replication_role         |ホストの役割(master/slave)
