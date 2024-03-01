resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'example'
  properties: {
    minimumTlsVersion: 'TLS1_0'
  }
}
