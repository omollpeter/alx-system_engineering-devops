# This puppet manifest edits a file and restart apache2 web server

exec { 'wordpress-edit':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => '/bin'
}
