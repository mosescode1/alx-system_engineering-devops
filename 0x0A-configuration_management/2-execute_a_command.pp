# Using Puppet, install flask from pip3.
exec { 'killmenow':
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow'
  refreshonly => true,
}
