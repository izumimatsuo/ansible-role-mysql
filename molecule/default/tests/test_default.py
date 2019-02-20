import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mysql_is_installed(host):
    mysql = host.package("mysql-community-server")
    assert mysql.is_installed
    assert mysql.version.startswith("5.6")


def test_mysql_running_and_enabled(host):
    mysql = host.service("mysqld")
    assert mysql.is_running
    assert mysql.is_enabled


def test_mysql_is_listen(host):
    assert host.socket("tcp://0.0.0.0:3306").is_listening
