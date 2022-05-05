exec{ 'fix-nginx':
      command  => 'sed -i "s/-n 15/-n 4096/g" /etc/default/nginx',
      provider => 'shell'
}
exec{'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
