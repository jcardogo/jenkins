file { '/etc/issue':
    mode => '0644',
    content => "Internal system \l \n",
}

exec { 'move example file':
    command => 'mv /home/users/example.txt /home/user/Desktop',
    onlyif => 'test -e /home/user/example.txt',
}
