# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  #config.vm.box = "debian/jessie64"
  config.vm.box = "ubuntu/trusty64"

  # Direct the Ansible Provision
  if ENV["ONLY_RUN_TEST"] 
    run_ansible(config.vm, "site.yml")
  end

  # Direct to run Tests
  if ENV["RUN_TESTS"] 
    puts "TESTS WILL BE EXECUTED AFTER INSTALLATION"
    #run_ansible(config.vm, "test/test_site.yml")
    run_ansible(config.vm, "roles/cassandra_users/test/test_main.yml")
  end
end

def run_ansible(vm, playbook)
  vm.provision "ansible" do |ansible|
    ansible.playbook = playbook
    ansible.compatibility_mode = "2.0"
  end
end
