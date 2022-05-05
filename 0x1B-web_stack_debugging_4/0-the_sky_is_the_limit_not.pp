exec{ 'fix-nginx':
  path    => '/bin',
  command => "sed -i 's/15/2000/g' /etc/default/nginx"
}
exec{'restart-nginx':
  path    => '/etc/init.d',
  command => 'nginx restart'
}
