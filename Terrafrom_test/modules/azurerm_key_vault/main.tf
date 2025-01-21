data "azurerm_client_config" "abc" {}

resource "azurerm_key_vault" "kv" {
  for_each                    = var.key_vaults
  name                        = each.value.kv_name
  location                    = each.value.location
  resource_group_name         = each.value.rg_name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.abc.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false

  sku_name = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.abc.tenant_id
    object_id = data.azurerm_client_config.abc.object_id

    key_permissions = [
      "Get",
    ]

    secret_permissions = [
      "Get", "Backup", "Delete", "Get", "List", "Purge", "Recover", "Restore", "Set"
    ]

    storage_permissions = [
      "Get",
    ]
  }
}

resource "azurerm_key_vault_secret" "my-secret" {
  name = "mysecret"
  value = "hello"
  key_vault_id = azurerm_key_vault.kv
  
}