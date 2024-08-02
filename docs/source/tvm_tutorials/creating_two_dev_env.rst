Creating two development environments
######################################

At the end of this tutorial, you will have two different TVM projects in two separate development environments.

Step by Step
-------------

#.  Install the latest stable release of TVM.

    .. code-block:: bash

        pip install git+https://github.com/eduNEXT/tvm.git

#.  Verify the installation.

    .. code-block:: bash

        tvm --version

#.  Create a new project with TVM.

    .. code-block:: bash

        tvm project init <project-name> <tutor-version>

        # For example:
        # tvm project init tvm-test v14.0.0

#.  Open the project folder.

    .. code-block:: bash

        cd <project-name>

#.  Activate the project environment.

    .. code-block:: bash

        source .tvm/bin/activate

#.  Run your project.

    .. code-block:: bash

        tutor dev launch

#.  Stop your project.

    .. code-block:: bash

        tutor dev stop

#.  Deactivate the project environment.

    .. code-block:: bash

        tvmoff

#.  Repeat steps 3 to 8 using the project-name and tutor-version you want.

.. note:: You can have as many projects as you want, but you can not have two projects with the same name and tutor version.

Next Steps
-----------

- To do more with TVM, check :doc:`TVM Topic Guides </tvm_topic_guides/index>`.
