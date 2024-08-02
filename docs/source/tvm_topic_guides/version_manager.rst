TVM as Tutor Manager
####################

Index
------
- `Install a Tutor version`_
- `Uninstall a Tutor version`_
- `Use a Tutor version`_
- `Configure the TUTOR_ROOT`_
- `Configure the TUTOR_PLUGINS_ROOT`_
- `Remove the TUTOR_ROOT and TUTOR_PLUGINS_ROOT variables`_
- `List Environments and Projects`_
- `Install Tutor Plugins`_
- `Uninstall Tutor Plugins`_

Install a Tutor version
------------------------

.. code-block:: bash

    tvm install <tutor-version>

    # For example:
    # tvm install v14.0.0

Uninstall a Tutor version
-------------------------

.. code-block:: bash

    tvm uninstall <tutor-version>

    # For example:
    # tvm uninstall v14.0.0

Use a Tutor version
--------------------

.. code-block:: bash

    tvm use <tutor-version>

    # For example:
    # tvm use v14.0.0

Configure the TUTOR_ROOT
-------------------------

.. code-block:: bash

    tvm config save <tutor root absolute path>

    # For example:
    # tvm config save /home/user/tutor-test
    # or
    # tvm config save .

Configure the TUTOR_PLUGINS_ROOT
---------------------------------

.. code-block:: bash

    tvm config save <tutor root absolute path> --plugins-root="ABSOLUTE PATH"

    # For example:
    # tvm config save /home/user/tutor-test --plugins-root="/home/user/tutor-test/plugins"
    # or
    # tvm config save . --plugins-root="/home/user/tutor-test/plugins"


Remove the TUTOR_ROOT and TUTOR_PLUGINS_ROOT variables
-------------------------------------------------------

.. code-block:: bash

    tvm config clear


List Environments and Projects
--------------------------------

.. code-block:: bash

    tvm list


.. note:: You can use the flag -l or --limit and an integer to restrict the output. E.g. ``tvm list --limit 10``


Install Tutor Plugins
----------------------

There are two ways to install Tutor plugins in your project.

TVM
^^^^

.. code-block:: bash

    tvm plugins install <plugin>


Pip
^^^^

.. code-block:: bash

    pip install <plugin>


.. note:: If you don't already have your project environment activated, you can activate it using ``source .tvm/bin/activate``, and then you will be able to use the pip command.


Uninstall Tutor Plugins
------------------------

There are two ways to uninstall Tutor plugins in your project.


TVM
^^^^

.. code-block:: bash

    tvm plugins uninstall <plugin>


Pip
^^^^

.. code-block:: bash

    pip uninstall <plugin>


.. note:: If you don't already have your project environment activated, you can activate it using ``source .tvm/bin/activate``, and then you will be able to use the pip command.


Related
--------

- :doc:`TVM as Environment Manager </tvm_topic_guides/environment_manager>`.
