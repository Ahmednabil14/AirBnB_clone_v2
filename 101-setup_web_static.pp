# Puppet manifest to set up web servers for the deployment of web_static

# Update apt repository
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

# Install nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}

# Create directories
file { ['/data/web_static/releases/test/', '/data/web_static/shared/']:
  ensure => 'directory',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Helle from Ngnix',
}

# Remove current symbolic link
file { '/data/web_static/current/':
  ensure => 'absent',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

# Change ownership
file { '/data/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Configure nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    server_name _;

    location / {
        index index.html index.nginx-debian.html;
    }
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
