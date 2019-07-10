## 0x08. Networking basics #1

### 0. Localhost 

What is localhost?

1. A hostname that means this IP
2. A hostname that means this computer
3. An IP attached to a computer

### 1. All IPs

What is 0.0.0.0?

1. All IPv4 addresses on the local machine
2. All the IPs
3. It means null in networking

### 2. Change your home IP 

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8.

### 3. Show attached IPs

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
```
sylvain@ubuntu$ ./3-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
```
### 4. Port listening on localhost

- Write a Bash script that listens on port 98 on localhost.

Starting my script.
```
sylvain@ubuntu$ sudo ./4-port_listening_on_localhost
```
- Connecting to localhost on port 98 using telnet and typing some text.
```
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```
- Receiving the text on the other side.
```
sylvain@ubuntu$ sudo ./4-port_listening_on_localhost
Hello world
test
```




