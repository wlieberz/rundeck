#!/bin/env bash

# Example of a very simple script to backup jobs in Rundeck.
# Requires rundeck-cli to be installed.

export RD_URL=http://rundeck:4440
export RD_COLOR=0

export RD_PROJECT=test-project-1
backup_file="./rundeck-jobs_backups/test-project-1/from-simple-backup_jobs.xml"
rd jobs list -f "$backup_file"

export RD_PROJECT=Project-2
backup_file="./rundeck-jobs_backups/Project-2/from-simple-backup_jobs.xml"
rd jobs list -f "$backup_file"
