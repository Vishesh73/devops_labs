resource "azurerm_storage_account" "storage_account" {
  for_each                 = var.storage_account_details
  name                     = each.value.storage_name
  location                 = each.value.location
  resource_group_name      = each.value.resource_group_name
  account_tier             = "Standard"
  account_replication_type = each.value.account_replication_type

  tags = {
    environment = "dev"
  }
}
resource "azurerm_storage_container" "example" {
  depends_on = [ azurerm_storage_account.storage_account ]
  name                  = "mycontainer"
  storage_account_id    = azurerm_storage_account.example.id
  container_access_type = "private"
}