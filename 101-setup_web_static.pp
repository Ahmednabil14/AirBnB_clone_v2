# 101-setup_web_static.pp

# Ensure Nginx is installed
package { 'nginx':
 ensure => installed,
}

exec { 'mkdir':
    mkdir -p /data/web_static/shared/
    mkdir -p /data/web_static/releases/test/
    sudo chown -R ubuntu:ubuntu /data/
}
# Define the base directory for web_static
file { '/data':
 ensure => directory,
 owner => 'ubuntu',
 group => 'ubuntu',
 mode   => '0755',
}

# Create necessary directories for web_static
file { [
 '/data/web_static',
 '/data/web_static/releases',
 '/data/web_static/shared',
 '/data/web_static/releases/test',
]:
 ensure => directory,
 owner => 'ubuntu',
 group => 'ubuntu',
 mode   => '0755',
}

# Create a test HTML file
file { '/data/web_static/releases/test/index.html':
 ensure => file,
 owner   => 'ubuntu',
 group   => 'ubuntu',
 mode    => '0644',
 content => '<html>
 <head>
 </head>
 <body>
    Holberton School
 </body>
</html>',
}

# Ensure the symbolic link exists
file { '/data/web_static/current':
 ensure => link,
 target => '/data/web_static/releases/test',
 force => true,
}

# Configure Nginx to serve the content
file { '/etc/nginx/sites-available/hbnb_static':
 ensure => file,
 owner   => 'root',
 group   => 'root',
 mode    => '0644',
 content => template('hbnb_static.erb'),
}

# Enable the Nginx site
nginx::resource::vhost { 'hbnb_static':
 ensure       => present,
 www_root     => '/data/web_static/current',
 listen_port => 80,
 server_name => 'hbnb_static',
 index_files => ['index.html'],
 autoindex    => 'off',
 ssl          => false,
 require      => File['/etc/nginx/sites-available/hbnb_static'],
}

# Ensure Nginx is running
service { 'nginx':
 ensure     => running,
 enable     => true,
 hasrestart => true,
 hasstatus => true,
 require    => Package['nginx'],
}
