# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  #config.vm.box = "debian/jessie64"
  config.vm.box = "ubuntu/trusty64"

  # Direct Vagrant to install using the Ansible Provisioner
  unless ENV["ONLY_RUN_TESTS"] 
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
    run_ansible(config.vm, "roles/cassandra_users/test/test_main.yml")
    run_ansible(config.vm, "roles/cassandra_server/test/test_main.yml")
    #run_ansible(config.vm, "test/test_site.yml")
  end
end

def run_ansible(vm, playbook)
  vm.provision "ansible" do |ansible|
    ansible.playbook = playbook
    ansible.compatibility_mode = "2.0"
  end
end
