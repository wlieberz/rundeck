Role Name
=========

This role installs and configures Rundeck Community Edition. Also installs and configures nginx as a tls terminating reverse proxy.

For the reverse proxy to work these files must exist:

```

/etc/ssl/private/server.crt
/etc/ssl/private/server.key

```

Hint: for development purposes, see the `self-signed-tls-cert` role.

Role tested on Oracle Linux 7. The main task checks the distro version and runs the `oracle-linux-7-tasks.yml` task file if appropiate. 


Requirements
------------

N/A.

Role Variables
--------------

The following vars are used and have default values set in defaults/main.yml:

`rundeck_java_pkg`


Dependencies
------------

N/A.

Example Playbook
----------------

```

- hosts: rundeck_servers
  become: true
  roles:
    - rundeck-community-server-install-rpm-nginx-proxy

```


License
-------

BSD

Author Information
------------------

William Lieberz
