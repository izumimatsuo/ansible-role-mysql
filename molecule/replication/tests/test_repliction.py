import os
import time

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('instance-2')


def test_mysql_replication_status(host):
    command = 'mysql -u root -ppassword -e "SHOW SLAVE STATUS\\G"'

    count = 0
    while True:
        status = host.run(command + '|grep "Slave_IO_Running: Connecting"').rc
        count += 1
        if status != 0 or count > 10:
            break
        time.sleep(3)

    assert 0 == host.run(command + '|grep "Slave_IO_Running: Yes"').rc
    assert 0 == host.run(command + '|grep "Slave_SQL_Running: Yes"').rc
