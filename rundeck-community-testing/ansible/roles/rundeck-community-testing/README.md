Role Name
=========

Role tested on Oracle Linux 7. The main task checks the distro version and runs the `oracle-linux-7-tasks.yml` task file if appropiate. 

Installs an instance of Rundeck suitable for testing from an rpm from the official rundeck rpm repo.

Requirements
------------

N/A.

Role Variables
--------------

The following vars are used and have default values set in defaults/main.yml:

```

rundeck_java_pkg

rundeck_http_port
rundeck_http_port_state

rundeck_https_port
rundeck_https_port_state

```

Finally, `templates/rundeck-config.properties.j2` uses the var: `rundeck_server_fqdn.stdout` , which the oracle-linux-7 task play fetches from the endpoint via a call to `hostname -f`

Dependencies
------------

N/A.

Example Playbook
----------------

```

- hosts: testing_rundeck_servers
  become: true
  roles:
    - rundeck-community-testing

```


License
-------

BSD

Author Information
------------------

William Lieberz
