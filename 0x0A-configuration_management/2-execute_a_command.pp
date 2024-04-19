# Create a Puppet manifest to kill a process named "killmenow" using pkil

exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f /alx-system_engineering-devops/0x0A-configuration_management/killmenow',
  onlyif      => '/usr/bin/pgrep -f /alx-system_engineering-devops/0x0A-configuration_management/killmenow', # Check if the process is running before attempting to kill it
  refreshonly => true,
}
