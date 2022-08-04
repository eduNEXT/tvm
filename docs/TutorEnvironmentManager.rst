Tutor Environment Manager
#########################

Tutor environment manager allows you to create one project and set one version for it.

You will be able to continue using the `tutor version manager`_ commands in your project:

- tvm list
- tvm plugins list


Creating a project
------------------

To create a new project you should call ``tvm project init``, this configures a new tvm project in the current path and set your-project as ``TUTOR_ROOT`` and ``TUTOR_PLUGINS_ROOT``.  

You can create different projects with the same tutor version, you have 2 options:

- Use the global active version.

.. code-block:: bash  
    
    # Using the global active version
    
    mkdir your-project && cd your-project
    tvm project init
    
- Use a specific installed version, this creates a new folder with the ``project-name`` to host it.

.. code-block:: bash  
    
    # Specify the version
    
    tvm project init project-name v14.0.0
    


Activate / Deactivate a project
-------------------------------

To activate a project you should run

.. code-block:: bash
    
    source .tvm/bin/activate
    
    # Verify your environment is active [version@project]
    # That shoud look like: 
    
    [v14.0.0@project-name] os:~/project-name$
    
    
To disable a project you should run ``tvmoff``

If you also enable another environment like python virtualenv, you need to deactivate each virtual environment in order, that's means:

.. code-block:: bash
    
    # (venv) [v12.2.0@project-name] ->
    deactivate
    tvmoff

    # [v12.2.0@project-name] (venv) ->
    tvmoff
    deactivate
    
**Note:** If you forgot to deactivate it in order, you will need to restart your shell terminal.


Check your projects
--------------------

Use ``tvm list`` to check the projects that had been created.

.. image:: images/tvm_list_project.png


Manage a plugin in your project
-------------------------------

**Install**

To install a tutor plugin in the current tutor version you should use ``pip install <PLUGIN_NAME/or/PLUGIN_LOCAL_PATH/or/PLUGIN_REPO>``

.. code-block:: bash
    
    pip install tutor-plugin
    pip install /home/user/tutor-plugin
    pip install git+https://github.com/user/tutor-plugin@vx.x.x
    
    
**List**

List installed plugins with ``tvm plugins list`` or ``tutor plugins list``.


**Uninstall**

To uninstall a tutor plugin in your project use ``tvm plugins uninstall <PLUGIN_NAME>`` or  ``pip uninstall <PLUGIN_NAME>`` 

.. code-block:: bash
    
    pip uninstall tutor-plugin
    tvm plugins uninstall tutor-plugin



.. _tutor version manager: https://github.com/eduNEXT/tvm/blob/master/docs/TutorVersionManager.rst