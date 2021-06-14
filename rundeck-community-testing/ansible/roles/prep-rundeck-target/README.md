Role Name
=========

This role preps the test host so that the rundeck server can execute commands on it with full sudo rights (no password prompt for sudo). It does the following: 

- Ensures that the `%wheel ALL=(ALL)       ALL` line is commented from `/etc/sudoers`.
- Ensures that the `%wheel  ALL=(ALL)       NOPASSWD: ALL` line is uncommented.
- Ensures that the rundeck user exists on the target test host.
- Ensures that the rundeck user has a `.ssh` dir in their home dir.
- Fetches the rundeck users's public key from `/var/lib/rundeck/.ssh/id_rsa.pub` on the rundeck server. 
- Ensures the rundeck users's public is present in `authorized_keys` on the target host, with correct permissions.

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

- hosts: testing_rundeck_targets
  become: true
  roles:
    - prep-rundeck-target

```

License
-------

BSD

Author Information
------------------

William Lieberz
