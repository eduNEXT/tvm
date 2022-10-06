How to configure environment variables in TVM
##############################################

In this section, you will learn how to configure the environment variables for each project.

The project has two variables: ``TUTOR_ROOT`` and ``TUTOR_PLUGINS_ROOT``.

Index
------

- `Set the TUTOR_ROOT`_
- `Set the TUTOR_PLUGINS_ROOT`_
- `Remove the environment variables`_


Set the TUTOR_ROOT
-------------------

To set the TUTOR_ROOT, you need to use:

.. code-block:: bash

    tvm config save <tutor root absolute path>

    # For example:
    # tvm config save /home/user/tutor-test
    # or
    # tvm config save .


Set the TUTOR_PLUGINS_ROOT
---------------------------

By default TUTOR_PLUGINS_ROOT = TUTOR_ROOT/plugins. If you want to set a different TUTOR_PLUGINS_ROOT, you should use the flag  ``--plugins-root="PATH"``

.. code-block:: bash

    tvm config save <tutor root absolute path> --plugins-root="ABSOLUTE PATH"

    # For example:
    # tvm config save /home/user/tutor-test --plugins-root="/home/user/tutor-test/plugins"
    # or
    # tvm config save . --plugins-root="/home/user/tutor-test/plugins"


Remove the environment variables
---------------------------------

To remove the actual configuration of ``TUTOR_ROOT`` and ``TUTOR_PLUGINS_ROOT`` use:

.. code-block:: bash

    tvm config clear
