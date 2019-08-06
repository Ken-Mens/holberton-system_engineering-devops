# Kill a process with name `killmenow`
exec { 'kill killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
