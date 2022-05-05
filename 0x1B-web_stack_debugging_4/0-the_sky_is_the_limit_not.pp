exec{ 'fix-nginx':
  path    => [ '/usr/bin' , '/bin', '/usr/sbin', '/sbin' ],
  command => "sed -i 's/15/4100/g' /etc/default/nginx"
}
exec{'restart-nginx':
  path    => '/usr/bin',
  command => 'sudo service nginx restart'
}
