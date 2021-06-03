# Deploying a webapp

## Backend

- app to the server
  - scp
  - git
  - maven/npm/pip/whatever
- start it
  - prefer using a "webapp container" like tomcat or gunicorn
  - on a "high" port like 5000, 8000, 8080
- make it start on reboot
  - systemd
  - supervisord
  - ...

### or use containers

For example dockerize it.

## Frontend

- typically static files (HTML, CSS, JS)
- move them to the server (see above)
- serve them with a static webserver (nginx)

## Nginx

- static webserver
  - can server your frontend files
- reverse proxy
  - can proxy https (or http) traffic to your backend
- TLS SNI (server name indication) support (multiple SSL certificates per IP)
- HTTP/2
  - HTTP/3 / QUIC support in preview

... any other load balancer / reverse proxy can be used in clouds

## Firewall

- open ports 80 & 443 (+ any other required)

## DNS

Point the domain name to the IP address.

- A record - direct domain - ip assignment
- CNAME - "alias" - domain name alias - domain name assignment
  - for example create CNAME for www (www.foobar.com => foobar.com)

## SSL certificates

- use `certbot` to get a free Let's Encrypt certificate
  - `certbot-nginx` (or something similar) can also modify your nginx configuration
- redirect HTTP to HTTPS
- use HSTS, if possible
- add `certbot renew` to the crontab (or use a systemd timer)