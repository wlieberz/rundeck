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

4. Prep test host:

Assuming you have a test host available at `10.0.2.6` which rundeck can hit, you can prep the test host by running:

`ansible-playbook prep-test-target.yml`

Please see the readme for the role for more details about what it does: `ansible/roles/prep-rundeck-target/README.md`

# Notes:

## Webhooks:

After creating a job, it is simple to add a webhook to call the job. In the web GUI, go to `WEBHOOKS` in the left-hand navigation bar, then click the `Add` button to create a new webhook.

Once created, you can test calling the webhook via curl. If you created a webhook called `install-security-patches-rhel-5678`, you could call it with something like:

```

curl -L -X POST "http://rundeck.dev.lab.local:4440/api/38/webhook/<random unique string from rundeck goes here>#install-security-patches-rhel-5678"

```

In production, you would obviously want to lock this down and require authentication.
