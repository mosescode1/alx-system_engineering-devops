# Using Puppet, install flask from pip3.

package { 'flask':
  ensure => installed,
  version => '2.1.0',
  provider => 'pip3',
  install_options => ['-y'],
}
