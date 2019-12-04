from azure.keyvault import KeyVaultClient 
from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials
import json


credentials = ServicePrincipalCredentials(
    client_id = '...',
    secret = '....',
    tenant = '.....'
)

client = KeyVaultClient(credentials)
#resource_client.providers.register('Microsoft.KeyVault')

# VAULT_URL must be in the format 'https://<vaultname>.vault.azure.net'
# SECRET_VERSION is required, and can be obtained with the KeyVaultClient.get_secret_versions(self, vault_url, secret_id) API
secret_bundle = client.get_secret('KEYVAULTURI', 'KEYVAULTNAME', 'SECRET_VERSION')
secret = secret_bundle.value
#print(client.get_secret('KEYVAULTURI', 'KEYVAULTNAME', 'SECRET_VERSION'))
print(secret) 
b = open("data.json" , "w+")
b.write(secret)

f = open("data.json" , "r")
data = json.load(f)
print(data["Properties"]["Host"])
print(data["Properties"]["Port"])
print(data["Properties"]["Mode"])
print(data["Properties"]["User_Name"])
print(data["Properties"]["Cred_URI"])
print(data["Properties"]["Local_Path"])
print(data["Properties"]["Remote_Path"])
print(data["Properties"]["Files_Pattern"])
