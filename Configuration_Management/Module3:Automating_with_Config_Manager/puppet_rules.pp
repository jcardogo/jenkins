class sudo {
    package { 'sudo':
        ensure => present,
    }
}

class sysctl {
    #Make sure the directory exists, some distros don't have it 
    file {'/etc/sysctl.d': #Selected resource
        ensure => directory, #Atributes
    }
}

class timezone {
    file {'/etc/timezone': #Linux distro defining timezone
        ensure => file,  #Atribute
        content => "UTC\n" #Atribute
        replace => true, #Atribute
    }
}

class ntp { #Network Time Protocol
    package { 'npt':
        ensure => latest,
    }
    file { '/etc/ntp.conf':
        source => 'puppet://modules/ntp/ntp.conf'
        replace => true,
    }
    service { 'ntp':
        enable => true,
        ensure => running, 
    }
}