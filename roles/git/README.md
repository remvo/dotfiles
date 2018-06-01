git
===

Installs and configures git.

Requirements
------------

None

Role Variables
--------------

Available variables are listed below, along with default values:

    dotfiles_home: "{{ ansible_env.HOME}}/dotfiles"

    # Backup old .gitconfig file
    git_gitconfig_backup: yes

    # Name used in commit message
    git_full_name: ""

    # Github username
    git_user: ""

    # If you use github, the should be the same as the email
    git_email: ""

    # Add your custom git alias in 'key = value' format
    git_aliases: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: git }

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
