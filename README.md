
> :heavy_exclamation_mark: *SWIFT does not provide commercial support for the content of this repo*

```bash
##############################################################################
DISCLAIMER: THE CONTENT OF THIS REPO IS PROVIDED "AS-IS"
##############################################################################
```

This playbook is responsible for automating the creation Github Actions to build and deploy a container image to dockerhub
## Pre-requisites before you get started

### Dependencies

1. Ensure Python 3+ is installed, with the ``requests`` package also installed
2. A virtual machine running Ubuntu, Debian, Fedora, Centos, or RHEL 7+
3. Docker
4. Ansible 

## Running

When you're ready to execute this, do the following

1. Modify the provided `inventory` file. Add appropriate values that suit your environment in the various sections


```sh
ansible-playbook -i inventory create_workflow.yml
```
# github-actions-ansible
