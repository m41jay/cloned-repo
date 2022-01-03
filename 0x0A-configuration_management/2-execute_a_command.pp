# using puppet to create a manifest that kills a
# process named killmenow
exec { 'killmenow':
  onlyif  => 'pgrep -f killmenow',
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin'
}