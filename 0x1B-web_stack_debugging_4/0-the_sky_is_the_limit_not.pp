# Increase size so that nginx server can handle larger traffic
exec { 'sky is the limit size' :
  command => 'sed -i "s/15/9000/g" /etc/default/nginx; service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
