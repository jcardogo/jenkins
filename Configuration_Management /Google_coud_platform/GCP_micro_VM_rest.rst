POST https://compute.googleapis.com/compute/v1/projects/fist-cloud-steps-acardogo/zones/northamerica-northeast1-c/instances
{
  "canIpForward": false,
  "confidentialInstanceConfig": {
    "enableConfidentialCompute": false
  },
  "deletionProtection": false,
  "description": "",
  "disks": [
    {
      "autoDelete": true,
      "boot": true,
      "deviceName": "instance-20241126-145444",
      "diskEncryptionKey": {},
      "initializeParams": {
        "diskSizeGb": "10",
        "diskType": "projects/fist-cloud-steps-acardogo/zones/northamerica-northeast1-c/diskTypes/pd-balanced",
        "labels": {},
        "sourceImage": "projects/debian-cloud/global/images/debian-11-bullseye-v20241112"
      },
      "mode": "READ_WRITE",
      "type": "PERSISTENT"
    }
  ],
  "displayDevice": {
    "enableDisplay": false
  },
  "guestAccelerators": [],
  "instanceEncryptionKey": {},
  "keyRevocationActionType": "NONE",
  "labels": {
    "goog-ec-src": "vm_add-rest"
  },
  "machineType": "projects/fist-cloud-steps-acardogo/zones/northamerica-northeast1-c/machineTypes/e2-micro",
  "metadata": {
    "items": []
  },
  "name": "instance-20241126-145444",
  "networkInterfaces": [
    {
      "accessConfigs": [
        {
          "name": "External NAT",
          "networkTier": "PREMIUM"
        }
      ],
      "stackType": "IPV4_ONLY",
      "subnetwork": "projects/fist-cloud-steps-acardogo/regions/northamerica-northeast1/subnetworks/default"
    }
  ],
  "params": {
    "resourceManagerTags": {}
  },
  "reservationAffinity": {
    "consumeReservationType": "ANY_RESERVATION"
  },
  "scheduling": {
    "automaticRestart": true,
    "onHostMaintenance": "MIGRATE",
    "provisioningModel": "STANDARD"
  },
  "serviceAccounts": [
    {
      "email": "1078023424328-compute@developer.gserviceaccount.com",
      "scopes": [
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/trace.append"
      ]
    }
  ],
  "shieldedInstanceConfig": {
    "enableIntegrityMonitoring": true,
    "enableSecureBoot": false,
    "enableVtpm": true
  },
  "tags": {
    "items": [
      "http-server"
    ]
  },
  "zone": "projects/fist-cloud-steps-acardogo/zones/northamerica-northeast1-c"
}