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

## Ansible via Rundeck:

### Rundeck Target Nodes vs Ansible inventory groups:

Based upon observation, it appears that the way Rundeck's target node specification and Ansible's target specification work together is as a combination of the hosts specified in the Playbook and Rundeck's Target Nodes acting as a `--limit`.

In other words, if your Playbook has:

```

- name: Fancy Playbook
  hosts: webservers

```

and you try to run it via Rundeck with the Target Node set to a node not in the Ansible inventory host group `webservers`, e.g. you want to run it against `database-srv-01`, the Rundeck Job Execution will happily report that the job ran successfully, in the sense that Ansible ran with a return code of 0, but if you inspect the output from the Job Execution you will see:

```

PLAY [Test Playbook For Rundeck] ********
skipping: no hosts matched

```

This is the same output that would result if you manually invoked the Ansible run with:

`ansible-playbook test-playbook.yml --limit database-srv-01`


For this reason, it might be less confusing to agree upon a convention within the team. For example, the convention could be to write all Playbooks for Rundeck execution with `hosts: all` and then limit execution via Rundeck Target Nodes.

On the other hand, it might make sense to leave the host specification as `hosts: webservers` if the Playbook should absolutely not be run on any hosts that aren't in the webservers group, just as an extra guardrail. This probably makes more sense if Rundeck and Ansible are using the same inventory source, e.g. Rundeck is using the "Ansible Resource Model Source".

### Nodes in Rundeck:

When using the Ansible Resource Model Source, if you allow Rundeck to Gather Facts, the Nodes in Rundeck will be populated with a useful subset of the Facts which Ansible gathered. The Ansible Inventory Group becomes a Rundeck Tag.

A Rundeck Node filter can be constructed from any of the Facts gathered, e.g.:

```

distribution: OracleLinux distribution_major_version: 7

```
