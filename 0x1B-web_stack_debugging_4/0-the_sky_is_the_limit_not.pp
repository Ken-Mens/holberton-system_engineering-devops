# Increase size so that nginx server can handle larger traffic
exec { 'sky is the limit size' :
  command => 'sed -i "s/15/9000/g" /etc/default/nginx; sudo service nginx restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}