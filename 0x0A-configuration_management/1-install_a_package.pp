#This manifest install a package flask from pip3
package { 'pip3':
    ensure   => 'installed'
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['pip3']
}
