# Bash script to change the OS configuration to open a file with no error message.
exec { 'Limit-modification':
  command =>  'echo -e "holberton hard nofile 2500\nholberton soft nofile 25000" > /etc/security/limits.conf',
  path    =>  ['/bin', '/usr/bin', '/usr/sbin']
}
