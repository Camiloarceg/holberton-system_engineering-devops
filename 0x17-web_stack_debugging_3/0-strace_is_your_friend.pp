# fixing error 500 using puppet config file typo.
exec {'fix-typo':
      command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
      path    => '/bin/',
}
