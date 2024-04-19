# creating a file in /tmp
$file_path = '/tmp/school'

file { $file_path:
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}

