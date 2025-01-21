resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacct"
  resource_group_name       = "rg"
  location                 = "eastus"
  account_tier              = "Standard"
  account_replication_type = "LRS"

  lifecycle {
    # Prevent accidental deletion
    prevent_destroy = true

    # Ignore changes to the tags attribute
    ignore_changes = [
      tags,
    ]
  }
}
