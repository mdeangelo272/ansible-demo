# Ansible Demo
This repository contains a sample Ansible Module, Role, and Playbook developed using best practices for Python and Ansible. 

## Setup
* Python 3.6.1
* pip 10.0.1
* Ansible 2.5.5

## Doc Notes
* Ansible Config turns on fact caching to allow for faster execution during development
* define ENV VARS
  * `RUN_TESTS`
  * `ONLY_RUN_TEST`

## TODO
* [ ] Add tests for cassandra server and open jdk
* [ ] 


## Running Notes
* debian install pip
apt install python-pip
* ubuntu cass driver deps
sudo apt-get install build-essential python-dev libev4 libev-dev

* testing for dependencies snippet:

vagrant@vagrant-ubuntu-trusty-64:~$ apt list python-pip
Listing... Done
python-pip/trusty-updates,now 1.5.4-1ubuntu4 all [installed]
