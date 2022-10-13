Creating two development environments
######################################

At the end of this Tutorial, you will have two different TVM Projects to have two development environments.

Step by Step
-------------

1. Install the latest stable release of TVM.


.. code-block:: bash

    pip install git+https://github.com/eduNEXT/tvm.git


2. Verify the installation.

.. code-block:: bash

    tvm --version

3. Install the version of Tutor you want to use.

.. code-block:: bash

    tvm install <tutor-version>

    # For example:
    # tvm install v14.0.0

4. Create a new project with TVM.

.. code-block:: bash

    tvm project init <project-name> <tutor-version>

    # For example:
    # tvm project init tvm-test v14.0.0

5. Open the project folder.

.. code-block:: bash

    cd <project-name>

6. Activate the project environment.

.. code-block:: bash

    source .tvm/bin/activate

7. Run your project.

.. code-block:: bash

    tutor dev quickstart

8. Stop your project.

.. code-block:: bash

    tutor dev stop

9. Deactivate the project environment.

.. code-block:: bash

    tvmoff

10. Repeat steps 3 to 8 using the project-name and tutor-version you want.

.. note::  You can have as many projects as you want, but you can't have two projects with the same name and tutor version.

Next Steps
-----------

- To do more with TVM, check :doc:`TVM Topic Guides </tvm_topic_guides/index>`.
