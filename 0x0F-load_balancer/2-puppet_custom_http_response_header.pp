# This manifest installs and configures nginx server

# Update the apt cache
exec { 'apt update':
        command => '/usr/bin/apt update'
}

# Ensure nginx is installed
package { 'nginx':
        ensure  => 'installed',
        require => Exec['apt update']
}

# Check the document root
file { '/var/www/html':
        ensure => 'directory',
        owner  => 'www-data',
        group  => 'www-data',
        mode   => '0755'
}

# Create basic content to be displayed on the default page
file { '/var/www/html/index.html':
        ensure  => present,
        owner   => 'www-data',
        group   => 'www-data',
        mode    => '0644',
        content => @(CONTENT)
Hello World!
        CONTENT
}

file { '/usr/share/nginx/html/custom_404.html':
        ensure  => present,
        owner   => 'root',
        group   => 'root',
        mode    => '0644',
        content => @(CONTENT)
Ceci n'est pas une page
        CONTENT
}

# Define the web servers configurations
file { '/etc/nginx/sites-available/default':
        ensure  => 'present',
        owner   => 'root',
        group   => 'root',
        content => @(CONTENT)
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Pages to serve (The first that is present
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /usr/share/nginx/html;
                internal;
        }

        location / {
                try_files $uri $uri/ =404;
                add_header X-Served-By $HOSTNAME;
        }

        rewrite ^/redirect_me$ https://www.youtube.com/watch?v=nIb22KNpuM4 permanent;
}
        CONTENT
}

# Ensure the symbolic link is present
file { '/etc/nginx/sites-enabled/default':
        ensure => 'link',
        target => '/etc/nginx/sites-available/default'
}

# Ensure the nginx.service is enabled and running and can be restarted
service { 'nginx':
        ensure     => 'running',
        enable     => true,
        hasrestart => true,
}
