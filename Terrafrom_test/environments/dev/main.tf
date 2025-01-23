

module "storage" {
  source = "../../modules/azurerm_storage_account"
 storage_account_details = var.storage_account_details
}


module "kv" {
  source = "../../modules/azurerm_key_vault"
  key_vaults = var.key_vaults
  
}

module "vnet" {
  source = "../../modules/azurerm_virtual_network"
  vnet_details = var.vnet_details
}

resource "azurerm_public_ip" "pip" {
  for_each = var.linux_vm
  name                = each.value.pip_name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  allocation_method   = each.value.allocation_method
}

# resource "azurerm_virtual_network" "vnet1" {
#   for_each = var.linux_vm
#   name                = each.value.virtual_network_name
#   address_space       = each.value.address_space
#   location            = each.value.location
#   resource_group_name = each.value.resource_group_name
# }

resource "azurerm_subnet" "frontend_subnet" {
  for_each = var.linux_vm
  depends_on = [ azurerm_virtual_network.vnet1 ]
  name                 =  each.value.subnet_name
  resource_group_name  = each.value.resource_group_name
  virtual_network_name = azurerm_virtual_network.vnet1.name
  address_prefixes     = each.value.address_prefixes
}

resource "azurerm_network_interface" "nic" {
  for_each = var.linux_vm
  name                = each.value.nic_name
  location            = each.value.location
  resource_group_name = each.value.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.frontend_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.pip.id
  }
}

resource "azurerm_linux_virtual_machine" "frontend_vm" {
  for_each = var.linux_vm
  name                            = each.value.vm_name
  resource_group_name             = each.value.resource_group_name
  location                        = each.value.location
  size                            = each.value.vm_size
  admin_username                  = each.value.admin_username
  # admin_password                  = "P@ssw01rd@123"
  disable_password_authentication = false
  network_interface_ids           = [azurerm_network_interface.nic.id]

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}
