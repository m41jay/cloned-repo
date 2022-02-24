# Update limit in the /etc/default/nginx file uaing Puppet
exec { 'update_ulimit':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 15000\"/g" /etc/default/nginx; service nginx restart',
  path    => '/usr/local/sbin/:/usr/local/bin/:/usr/sbin:/usr/bin:/sbin:/bin',
}
