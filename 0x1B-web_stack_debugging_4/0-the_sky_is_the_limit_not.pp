# Update limit in the /etc/default/nginx file uaing Puppet
exec { 'update_ulimit':
  command => 'sed -i \'s/15/15000/\' /etc/default/nginx && service nginx restart',
  path    => [ '/bin/', /sbin/', '/usr/bin/', '/usr/sbin/' ]
}
