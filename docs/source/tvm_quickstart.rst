Quickstart
###########

Let's start by configuring and running our first project.

Index
------
- `Requirements`_
- `Step by Step`_
- `Next Steps`_

Requirements
-------------

TVM works with Tutor for that reason the Tutor requirements are also the TVM requirements.

**Basic Requirements:**

- Software:
    - `Docker <https://docs.docker.com/engine/installation/>`_: v24.0.5+ (with BuildKit 0.11+)
    - `Docker Compose <https://docs.docker.com/compose/install/>`_: v2.0.0+
- Hardware:
    - Minimum configuration: 4 GB RAM, 2 CPU, 8 GB disk space
    - Recommended configuration: 8 GB RAM, 4 CPU, 25 GB disk space

For more information, see the `Tutor requirements <https://docs.tutor.overhang.io/install.html#requirements>`_.


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

        tutor local launch
        
.. note:: For Tutor versions <15, init a project with ``tutor local quickstart```


Next Steps
-----------

- To do more with TVM, check :doc:`Tutorials </tvm_tutorials/index>` or :doc:`TVM Topic Guides </tvm_topic_guides/index>`.
- To know more about Tutor, check `Tutor documentation <https://docs.tutor.overhang.io/>`_.
