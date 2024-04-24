# This manifests installs and configures nginx server
exec { 'apt update':
    command => '/usr/bin/apt update'
}

package { 'nginx':
    ensure  => 'installed'
    require => Exec['apt update']
}

service { 'nginx':
    ensure  => 'running',
    require => Package['nginx']
}

$doc_root = '/var/www/html'

file { $doc_root:
    ensure => 'directory'
}

file { '$doc_root/index.html':
    ensure  => 'present',
    content => 'Hello World!',
    require => File[$doc_root]
}

file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => template('default.erb'),
    notify  => Service['nginx'],
}

exec { 'restart':
    command => 'sudo /etc/init.d/nginx restart'
}
