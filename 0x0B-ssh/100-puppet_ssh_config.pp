# set up my client ssh configuration file
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ss/ssh_config':
  path  => '/bin/'
}
