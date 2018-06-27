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
# from ansible.module_utils.six import binary_type, text_type
# from ansible.module_utils.six.moves import configparser


try:
    from cassandra.cluster import Cluster
    CASSANDRA_FOUND = True
except ImportError:
    CASSANDRA_FOUND = False

def get_session():
    session = None
    try:
        # todo add logic to use the params
        cluster = Cluster()
        session = cluster.connect()
    except: 
        module.fail_json(msg="Unable to login to cluster")

    return session

def keyspace_exists(session, name):
    # todo: add logic to determine if the keyspace exists
    return False

def create_keyspace(session, name):
    statement = "CREATE KEYSPACE {0} WITH REPLICATION = {{'class' : 'SimpleStrategy', 'replication_factor': 1}};"
    # todo: add error handling
    session.execute(statement.format(name)

def drop_keyspace(session, name):
    statement = "DROP KEYSPACE {0};"
    # todo: add error handling
    session.execute(statement.format(name)

def main():
    # create and configure the Ansible Module instance
    module = AnsibleModule(
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
        module.fail_json(msg="the python package cassandra-driver is required")

    changed = False  
    name = module.params['name']
    state = module.params['state']

    # get an active session
    session = get_session()

    # test if the keyspace exists
    exists = keyspace_exists(name)

    # todo: mkd - add logic to create and remove keyspace
    # * add logic to log into server and report failures
    # * add logic to determine if the keyspace exists
    # * add conditional logic to add/remove the keyspace based on the 'state' flag
    #   and existance of the keyspace in Cassandra

    module.exit_json(changed=changed, name=name)


if __name__ == '__main__':
    main()
