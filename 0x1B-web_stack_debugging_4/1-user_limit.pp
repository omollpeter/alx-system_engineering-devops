# This manifest removes the limit restriction on a specific user

exec { 'allow-holberton':
    command => "sed -i '/holberton/d' /etc/security/limits.conf",
    path    => '/bin'
}
