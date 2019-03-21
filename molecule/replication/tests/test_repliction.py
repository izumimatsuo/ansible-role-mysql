import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('instance-2')


def test_mysql_replication_status(host):
    command = 'mysql -u root -ppassword -e "SHOW SLAVE STATUS\G"'
    assert 0 == host.run(command + '|grep "Slave_IO_Running: Yes"').rc
    assert 0 == host.run(command + '|grep "Slave_SQL_Running: Yes"').rc
