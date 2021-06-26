Role Name
=========

Installs Rundeck in the simplest form: using the built-in DB, and serving Rundeck directly from rundeckd on the default http port (4440) i.e., http://rundeck.server.fqdn:4440.


Requirements
------------

N/A.

Role Variables
--------------

The following vars are used and have default values set in defaults/main.yml:

`rundeck_java_pkg: "java-11-openjdk.x86_64"`

Override this, as needed.

Dependencies
------------

N/A.

Example Playbook
----------------

```

- hosts: testing_rundeck_servers
  become: true
  roles:
    - rundeck-community-server-install-rpm-4440-http

```


License
-------

BSD

Author Information
------------------

William Lieberz
