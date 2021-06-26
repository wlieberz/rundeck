#!/bin/bash

# For dev only - do not use in Prod!

# Generate key and csr:
openssl req -new -config csr-conf.cnf \
  -keyout server.key \
  -out server.csr

# Self-sign with existing key and csr:
openssl x509 \
       -signkey server.key \
       -in server.csr \
       -req -days 365 -out server.crt

# Ensure key file is secure:
chmod 440 server.key
