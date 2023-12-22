# install flask with puppet
exec { 'install flask':
  command => 'pip install flask==2.1.0',
  path => 'usr/bin',
}
