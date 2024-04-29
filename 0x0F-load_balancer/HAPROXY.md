An HAProxy configuration file is composed of sections like **frontend, backend, defaults, and global.**

**FRONTEND**

this section defines the ipaddress and port that clients can connect to, Many frontend sections can be added as needed

```apache
frontend myfrontend
	# sets the proxy mode to either layer 7(HTTP) or layer 4(TCP)
	mode http
	# Recives all traffic bounded to port 80
	bind *:80
	# chose the default server of backend
	use_default web_servers
```

A frontend can listen to multiple IP addresses

```apache
frontend myfrontend
  mode http
  bind 192.168.1.5:80
  bind 192.168.1.6:80
  default_backend web_servers
```

listening to both port 80 and 433

```apache
frontend myfrontend
  mode http
  bind :80
  bind :443 ssl crt /site.pem

  # Redirect HTTP to HTTPS
  http-request redirect scheme https unless { ssl_fc }

  default_backend web_servers
```

use multiple frontend for different traffic types

```apache
frontend foo.com
  mode http
  bind 192.168.1.5:80
  default_backend foo_servers
frontend db.foo.com
  mode tcp
  bind 192.168.1.15:3306
  default_backend db_servers
```

Frontend `db.foo.com` has been configured to receive TCP traffic, in this case MySQL traffic at port 3306, and cannot make use of Layer 7 inspection and routing. Therefore, `mode` is set to `tcp`, which enables a simpler Layer 4 proxying.
