# Change Os configuration user limit
exec { 'chage-os-configuration':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  command => 'sed -i "/holberton soft nofile 4/a holberton - nofile 65535\nholberton = nproc 65535" /etc/security/limits.conf; sudo reboot'
# 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/g" /etc/security/limits.conf; \
# sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/g" /etc/security/limits.conf;',
}
