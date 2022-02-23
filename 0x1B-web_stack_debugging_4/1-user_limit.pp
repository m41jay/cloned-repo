# Change Os configuration user limit
exec { 'Correct hard':
  command  => "sudo sed -i 's/holberton hard nofile 4/holberton hard nofile 88888/g' /etc/security/limits.conf",
  provider => shell
}

exec { 'Correct soft':
  command  => "sudo sed -i 's/holberton soft nofile 5/holberton soft nofile 88888/g' /etc/security/limits.conf",
  provider => shell
}
