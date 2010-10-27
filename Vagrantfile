Vagrant::Config.run do |config|
  config.vm.box = "lucid32"
  config.vm.box_url = "http://files.vagrantup.com/lucid32.box"
  config.vm.customize do |vm|
    vm.name = "QMLShopper"
  end
  config.vm.provisioner = :chef_solo
  config.chef.cookbooks_path = 'chef-cookbooks/cookbooks'
  config.chef.add_recipe('scratchbox')
end
