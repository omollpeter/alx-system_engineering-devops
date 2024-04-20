# This manifest makes changes to SSH client configuration file
exec { 'puppetlabs-ssh':
    command => 'puppet module install puppetlabs-ssh'
}

class { 'ssh': }


ssh::client::config { 'ssh_config':
    ensure       => 'present',
    options_hash => {
        'IdentityFile'           => '~/.ssh/school',
        'PasswordAuthentication' => 'no'
    }
}
