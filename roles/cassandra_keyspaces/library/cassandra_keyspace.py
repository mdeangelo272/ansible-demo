#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: cassandra_keyspace
short_description: Will Add or remove a keyspace from Cassandra.
description:
    - This module will add or remove a keyspace from Cassandra.
version_added: "0.1"
options:
    login_user:
        description:
            - The user name used to login into Cassandra
    login_password:
        description:
            - The password used to login into Cassandra
    login_host:
        description:
            - The hostname or IP of the instance running Cassandra
        default: localhost
    login_port:
        description:
            - The port that Cassandra is listening for client traffic
        default: 9042
    name:
        description:
            - The name of the Cassandra Keyspace name
        required: true
    state:
        description:
            - The state of the Cassandra Keyspace
        default: present
        choices: ["present", "absent"]

notes:
    - Requires the 'cassandra-driver' Python package. @see https://docs.datastax.com/en/developer/python-driver/3.10/

'''

EXAMPLES = '''
# todo: mkd - add examples
'''

RETURNS = '''
name:
    description: The keyspace name affected.
    returned: success
    type: string
'''

from ansible.module_utils.basic import AnsibleModule

try:
    from cassandra.cluster import Cluster
    CASSANDRA_FOUND = True
except ImportError:
    CASSANDRA_FOUND = False


class CassandraKeyspace(object):
    """
    Uses AnsibleModule and the Cassandra Driver to modify Cassandra Keyspaces.
    """

    def __init__(self):
        self.module = AnsibleModule(
            argument_spec=dict(
                login_user=dict(),
                login_password=dict(no_log=True),
                login_host=dict(default='localhost'),
                login_port=dict(default=9042, type='int'),
                name=dict(required=True),
                password=dict(no_log=True),
                state=dict(default='present', choices=['present', 'absent'])
            ),
            supports_check_mode=False  # todo: add check mode support
        )

        # Validate that the cassanadra driver has been installed
        if not CASSANDRA_FOUND:
            self.module.fail_json(msg="the python package cassandra-driver is required")

        self.cluster = None
        self.session = None

        self.connect_to_cassandra()
        self.converge_state()

    def connect_to_cassandra(self):
        """
        creates and configures the Cassandra cluster
        """
        try:
            # todo add logic to use the params
            #   this requires creating a dictionary only populated with the not null-like values.
            #   The Cluster object does not handle null values very well
            self.cluster = Cluster()
            self.session = self.cluster.connect()
        except Exception as ex:
            self.module.fail_json(msg=str(ex))

    def execute_statement(self, statement):
        try:
            self.session.execute(statement)
        except Exception as ex:
            self.module.fail_json(msg=str(ex))

    def keyspace_exists(self, name):
        """
        Determines if the Keyspace Exists
        """
        return name in self.cluster.metadata.keyspaces

    def create_keyspace(self, name):
        """
        Creates the Keyspace
        """
        statement = "CREATE KEYSPACE {0} WITH REPLICATION = {{'class' : 'SimpleStrategy', 'replication_factor': 1}};"
        self.execute_statement(statement.format(name))

    def drop_keyspace(self, name):
        """
        Drops the Keyspace
        """
        statement = "DROP KEYSPACE {0};"
        self.execute_statement(statement.format(name))

    def converge_state(self):
        """
        Performs the primary business logic to add or remove Cassandra Keyspaces.
        """

        # stage common variables at this scope
        changed = False
        name = self.module.params['name']
        state = self.module.params['state']

        # test if the keyspace exists
        exists = self.keyspace_exists(name)

        # add or Drop the Keyspace based on criteria
        if not exists and state == 'present':
            self.create_keyspace(name)
            changed = True
        elif exists and state == 'absent':
            self.drop_keyspace(name)
            changed = True

        self.module.exit_json(changed=changed, name=name)


if __name__ == '__main__':
    CassandraKeyspace()
