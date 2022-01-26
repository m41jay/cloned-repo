# set up my client ssh configuration file
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
  path  => '/bin/'
}
