# Increase size so that nginx server can handle larger traffic
exec { 'limitsize' :
  command => 'sed -i "s/15/5000/g" /etc/default/nginx',
  path    => '/bin/',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
