variable "linux_vm" {
  type = map(any)
}

variable "storage_account_details" {
  type = map(any)
}

variable "key_vaults" {
  type = map(any)
}

variable "vnet_details" {
  type = map(any)
}


# Variables with Correct Data Types

# variable "resource_group_name" {
#   description = "The name of the resource group"
#   type        = string
#   default     = "my_rg"
# }

# variable "location" {
#   description = "The Azure region where the resources will be created"
#   type        = string
#   default     = "eastus"
# }

# variable "virtual_network_name" {
#   description = "The name of the virtual network"
#   type        = string
#   default     = "test_vnet"
# }

# variable "address_space" {
#   description = "The address space of the virtual network"
#   type        = list(string)
#   default     = ["10.0.0.0/16"]
# }

# variable "subnet_name" {
#   description = "The name of the subnet"
#   type        = string
#   default     = "internal"
# }

# variable "address_prefixes" {
#   description = "The address prefixes for the subnet"
#   type        = list(string)
#   default     = ["10.0.2.0/24"]
# }

# variable "vm_size" {
#   description = "The size of the virtual machine"
#   type        = string
#   default     = "Standard_DS1_v2"
# }

# variable "nic_name" {
#   description = "The name of the network interface"
#   type        = string
#   default     = "nic"
# }

# variable "admin_username" {
#   description = "The admin username for the virtual machine"
#   type        = string
#   default     = "adminuser"
# }

# variable "vm_name" {
#   description = "The name of the virtual machine"
#   type        = string
#   default     = "frontend_vm"
# }

# variable "pip_name" {
#   description = "The name of the public IP"
#   type        = string
#   default     = "pip"
# }

# variable "allocation_method" {
#   description = "The allocation method for the public IP"
#   type        = string
#   default     = "Static"
# }
