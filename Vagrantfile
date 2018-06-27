# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

	# cassandra will crash with the default memory size
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  # Direct Vagrant to install using the Ansible Provisioner
  unless ENV["SKIP_INSTALL"] 
    run_ansible(config.vm, "site.yml")
  else
    puts "*********************"
    puts "skipping installation"
    puts "*********************"
  end

  # Direct Vagrant to run the tests
  if ENV["RUN_TESTS"] 
    puts "**************************"
    puts "The tests will be executed"
    puts "**************************"
    run_ansible(config.vm, "test/test_site.yml")
  end
end

def run_ansible(vm, playbook)
  vm.provision "ansible" do |ansible|
    ansible.playbook = playbook
    ansible.compatibility_mode = "2.0"
  end
end
