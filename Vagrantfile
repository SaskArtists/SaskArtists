Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, path: "provision.sh"
  config.vm.network "private_network", ip: "10.0.0.10"
end
