# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
  config.vm.synced_folder ".", "/vagrant"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get -y upgrade
    apt-get install -y python-minimal
    #

    apt-get install -y libsnmp-dev
    apt-get install -y snmp-mibs-downloader
    apt-get install -y gcc
    apt-get install -y python-dev
    apt-get install -y python-pip
    apt-get install -y python-netsnmp
    apt-get update
    apt-get -y upgrade
    pip install pysnmp --user

#     apt-get install -y apache2
  SHELL
end
