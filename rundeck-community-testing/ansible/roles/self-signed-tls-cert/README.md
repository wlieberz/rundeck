Role Name
=========

Role does the following:

1. Ensure that /etc/ssl/private directory exists with root:root 750 permissions.
2. Puts a basic csr config filein the above dir.
3. Runs `generate-self-signed-tls-cert-and-key.sh` using the csr conf file copied earlier.

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

```

- hosts: foo_app_dev
  become: true
  roles:
    - self-signed-tls-cert

```
License
-------

BSD

Author Information
------------------

William Lieberz
