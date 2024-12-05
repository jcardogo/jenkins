"""node default {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
} /"""

node webserver.example.com { #in this case we have the node definition for a host 
  class { 'sudo': } 
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
   }
  class { 'apache': } #THis class will aplly apache module 
}