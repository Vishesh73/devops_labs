linux_vm = {
  vm1 = {
  resource_group_name = "my_rg"
  location = "eastus"
  virtual_network_name= "test_vnet"
  address_space       = ["10.0.0.0/16"]
  subnet_name = "internal"
  address_prefixes     = ["10.0.2.0/24"]
   vm_size               = "Standard_DS1_v2"
   nic_name = "nic"
   admin_username      = "adminuser"
   vm_name  = "frontend_vm"
   pip_name = "pip"
   allocation_method   = "Static"
  }
}

storage_account_details = {
  st1 = {
  resource_group_name = "my_rg"
  location = "eastus"
   account_replication_type = "LRS"
   storage_name = "mystorage"
}
}

key_vaults = {
  kv1 = {
  resource_group_name = "my_rg"
  location = "eastus"
  kv_name = "mykv"
}
}