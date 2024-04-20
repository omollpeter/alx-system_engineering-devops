# This manifest makes changes to SSH client configuration file
class my_ssh_config {
    include ssh::client

    file_line { 'PasswordAuthentication':
        path    => '/etc/ssh/ssh_config',
        value   => 'no',
    }

    file_line { 'IdentityFile':
        path    => '/etc/ssh/ssh_config',
        value   => '~/.ssh/school'
    }
}
