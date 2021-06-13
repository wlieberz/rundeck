# About:

Tested on Oracle Linux 7, with Rundeck Community 3.3.12.

Note: per the Rundeck documentation, since no other database is configured, it just uses an H2 embedded database, not suitable for production use.

Also, this ansible role does not take care of provisioning a TLS certificate, so access on the https port will not work.

Please see Rundeck's docs:

https://docs.rundeck.com/docs/administration/install/

# Setup:

## Oracle Linux 7 VM:

1. Ensure you have an Oracle Linux 7 VM installed, with all the latest patches. This project assumes you can reach it via the flat name "rundeck" either via an `/etc/hosts` entry or local DNS. Feel free to configure with a fully qualified domain name, and adjust the ansible inventoryas needed (`ansible/hosts`).

2. Ensure you have Ansible installed, cd into the ansible directory and run:

`ansible-playbook site.yml`

3. If all went well, you should be able to login to the rundeck url.

URL: http://rundeck:4440/

Username: admin
Initial Password: admin
