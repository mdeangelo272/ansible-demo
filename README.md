# Ansible Demo

![Cassandra Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/200px-Cassandra_logo.svg.png)

This repository contains a sample Ansible Module, Role, and Playbook that will install a Cassandra database and manage Cassandra database users. 

## Setup and Dependencies
This solution was implemented and testing using the software and versions listed below. Note that these are the versioned used on the development machine (i.e. the controlleror host node). 
* Python 3.6.1
  * pip 10.0.1
* Ansible 2.5.5
* VirtualBox 5.2.12
* Vagrant 2.1.1

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
