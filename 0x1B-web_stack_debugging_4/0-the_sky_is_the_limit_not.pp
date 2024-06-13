# This puppet manifest increases the max open files limit by editing /etc/default/nginx

service { 'nginx':
    ensure => 'running',
    enable => true
}

exec { 'edit-default-nginx':
    command => "sed -i 's/-n 15/-n 4096/' /etc/default/nginx",
    path    => '/bin',
    notify  => Service['nginx']
}
