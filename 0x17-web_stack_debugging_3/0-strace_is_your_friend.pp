# fixes the internal server error of apache
exec{'fixing':
  command=> 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
  path=> '/usr/local/bin:/bin/'
}
