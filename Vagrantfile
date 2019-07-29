# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
  config.vm.synced_folder ".", "/vagrant"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get -y upgrade
    #
    # https://linoxide.com/linux-how-to/install-python-ubuntu/
    apt-get install -y python3
    #
    apt-get -y upgrade
    #
    apt-get -y install python3-pip
    apt-get update
    #
    apt-get install net-snmp-python
    #
    pip3 install snmp 
    pip3 install snmp-cmds
    #
    
    apt-get install libsnmp-dev snmp-mibs-downloader

    #     apt-get install -y apache2
  SHELL
end
