genkeys
=======

This bash script is a wrapper around the dnssec-keygen tool that comes with BIND named. It allows you to generate, update, and prepublish ZSK and KSK key pairs for DNSSEC deployment for all your existing zone files in a single run. The default values should work out-of-the-box on CentOS 6.
