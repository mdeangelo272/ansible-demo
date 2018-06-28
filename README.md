# Ansible Demo

![Cassandra Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/500px-Cassandra_logo.svg.png)

This repository contains a sample Ansible Module, Role, and Playbook that will install a Cassandra database and manage Cassandra database keyspaces. 

## Setup and Dependencies
This solution was implemented and tested using the software and versions listed below. Note that these are the versions used on the development machine (i.e. the controller or host node), not necessarily the versions installed by the configuration logic. 
* Python 3.6.1 and pip 10.0.1
* Ansible 2.5.5
* VirtualBox 5.2.12
* Vagrant 2.1.1

If you would like instructions on how to install these tools or how to use them please [create a new issue](https://github.com/mdeangelo272/ansible-demo/issues/new) or [email me](mailto:iam@mdeangelo272.me).

## Usage
This demo solution is intended to be completely self-contained. To install Cassandra and create a demo keyspace simply run:
```
vagrant up
```
from the repos root directory (denoted `./` through the rest of the README). This will:
* Create a new Ubuntu 14.04 LTS VM instance in virtualbox
* Execute the Ansible Provisioner and run the `site.yml` playbook. 

Executing the automated tests can be performed with 2 environment variable flags:
* `RUN_TESTS` - Informs Vagrant to run the automated tests
* `SKIP_INSTALL` - Informs Vagrant to skip the install. This is helpful when you only want to run the tests. 

For example, if you want to only run the tests and skip the install logic you could run:
``` 
RUN_TESTS=1 SKIP_INSTALL=1 vagrant provision
```

## Solution Overview
This solution consistings of a global `site.yml` playbook that performs all installation and configuration operations as well as [Ansible Roles](https://docs.ansible.com/ansible/2.5/user_guide/playbooks_reuse_roles.html). The high level structure is: 

```
todo: mkd - update this will new role
todo: add description of new roles
.
├── LICENSE
├── README.md
├── Vagrantfile
├── ansible.cfg
├── roles
│   ├── cassandra_server
│   │   ├── handlers
│   │   ├── meta
│   │   ├── tasks
│   │   ├── templates
│   │   ├── test
│   │   └── vars
│   ├── cassandra_keyspaces
│   │   ├── library
│   │   ├── meta
│   │   ├── tasks
│   │   ├── test
│   │   └── vars
│   └── common
│       └── defaults
├── site.yml
├── test
├── vars
│   └── vault
└── vault_password
```

Note that this demo solution uses `Ansible-Vault` to manage password. These are stored in `./vars/vault` and the vault password is stored in `./vault_password`. **This is for demo purposes only, NEVER store unencyrpted passwords or private keys in an SCM repository!**


### Roles
The solution consists of 3 Roles: 
* `common` - This is a very thin Role that only stores `default` values for some common variables. 
* `cassandra_server` - This install the Cassandra Server and it's dependencies. It is based on the [Cassandra Installation Guide](http://cassandra.apache.org/doc/latest/getting_started/installing.html). 
* `cassandra_keyspace` - This is the most sophisticated role. It is responsible for managing keyspaces in the Cassandra database. It includes a custom Ansible Module that can add and remove cassandra keyspaces. 

### Custom Module
The Custom Ansible module is defined in `./roles/cassandra_keyspaces/library/cassandra_keyspace.py`. It is also possible to define modules in a common location, but a Role was chosen to increase the modularity of the solution. It depends on the [cassandra-driver](https://github.com/datastax/python-driver/) python package. The Role is responible for installing this dependency. Note, that modules run on the target node not the controlller node. Thus, for large scale solutions the Role and Module should be run on a dedicated hosts group (defined in a inventory file) or on the controller node itself using node delegation or local execution. 

The module is intended to pass `flake8` tests, but the `tox.ini` defines exceptions in the PEP8 standard that are common to Ansible. One can also create a symbolic link to the module to allow for global visibility to the Ansible tools. If this is done you can use the `ansible-doc` command to view the integrated documentation. 
```
$ ansible-doc cassandra_keyspace
> CASSANDRA_KEYSPACE    (~/.ansible/plugins/modules/cassandra_keyspace.py)

        This module will add or remove a keyspace from Cassandra.

OPTIONS (= is mandatory):

- login_host
        The hostname or IP of the instance running Cassandra
        [Default: localhost]

- login_password
        The password used to login into Cassandra
        [Default: (null)]

- login_port
        The port that Cassandra is listening for client traffic
        [Default: 9042]

- login_user
        The user name used to login into Cassandra
        [Default: (null)]

- state
        The state of the Cassandra Keyspace
        (Choices: present, absent)[Default: present]

= name
        The name of the Cassandra Keyspace


NOTES:
      * Requires the 'cassandra-driver' Python package. @see https://docs.datastax.com/en/developer/python-driver/3.10/

        METADATA:
          status:
          - preview
          supported_by: community


EXAMPLES:
# todo: mkd - add examples
```

## TODO
* [x] Add logic and tests to install cassandra and it's dependencies
* [x] Add logic and tests to install dev tools and pip (system dependencies for cassandra-driver)
* [x] Track down remaining dependency for cassandra-driver (this was working but didn't survive a `vagrant destroy` there is a manually step I need to track down)
* [x] Finish the custom Ansible Module to modify Cassandra Keyspaces
  * [x] Add logic to exercise the Module and create a demo Keyspace
  * [x] Add testing logic to validate that the module is idempotent
* [ ] Update README to reflect new Role structure
* [ ] Document that the module needs to be sym linked for tests to work, for fix that requirement
```
mkdir -p ~/.ansible/plugins/modules
ln -s ~/dev/repos/mdeangelo272/ansible-demo/roles/cassandra_keyspaces/library/cassandra_keyspace.py ~/.ansible/plugins/modules/
```
* [ ] Add assertion logic in the modules tests
* [ ] Add logic to actually use the params in the module



## Issues and PRs
To report issues or ask questions about this repo please feel free to create an issue [here](https://github.com/mdeangelo272/ansible-demo/issues/new). Please also feel free to offer enhancements and suggestions in the form of [Pull Requests](https://github.com/mdeangelo272/ansible-demo/pulls).


