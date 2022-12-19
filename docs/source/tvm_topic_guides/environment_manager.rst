TVM as Environment Manager
###########################

Index
------

- `Create a Project`_
- `Remove a Project`_
- `Activate a Project Environment`_
- `Deactivate a Project Environment`_
- `List Environments and Projects`_
- `Install Tutor Plugins`_
- `Uninstall Tutor Plugins`_


Create a Project
-----------------

.. code-block:: bash

    tvm project init <project-name> <tutor-version>

    # For example:
    # tvm project init tvm-test v14.0.0


.. note:: The <tutor-version> parameter is optional. However, if you don't specify the version, the project will be created with the version you set previously with tvm use <tutor-version> or the latest version. If you specify the version, and the version isn't installed, it will be installed.


Remove a Project
-----------------

.. code-block:: bash

    tvm project remove <project-name> <tutor-version>

    # For example:
    # tvm project remove tvm-test v14.0.0


.. note:: You can use the flag --prune to remove all the project folder. Ex: `tvm project remove tvm-test v14.0.0 --prune`


Activate a Project Environment
------------------------------

.. code-block:: bash

    source .tvm/bin/activate


Deactivate a Project Environment
--------------------------------

.. code-block:: bash

    tvmoff


.. warning:: If you also have another environment like a python virtual environment, you need to deactivate each virtual environment in order. For example, if you have `(venv) [v12.2.0@project-name]`, you need to run `deactivate` and then `tvmoff`.

List Environments and Projects
--------------------------------

.. code-block:: bash

    tvm list


.. note:: You can use the flag -l or --limit and an integer to limit the output. Ex: `tvm list --limit 10`

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


.. note:: If you don't already have your project environment activated, you can activate it using `source .tvm/bin/activate`, and then you will be able to use the pip command.


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


.. note:: If you don't already have your project environment activated, you can activate it using `source .tvm/bin/activate`, and then you will be able to use the pip command.


Related
--------

- :doc:`TVM as Tutor Manager </tvm_topic_guides/version_manager>`.
