# What's TVM
TVM is the acronym of Tutor Version Manager. It manages Tutor versions and enables switching between them.

# Installing TVM

## GitHub
```bash
pip install git+https://github.com/eduNEXT/tvm.git@<TAG/or/BRANCH>
```

# Upgrading TVM (ToDo)
Currently, there isn't a command to do it, if you want to upgrade it, please install it again.

# Basic TVM usage
Basic TVM usage scenarios include installing and switching between different tutor versions.

## Installing tutor
To install tutor you have to call `tvm install v<TUTOR_VERSION>`, if you don't know which are the
tutor versions, you can call `tvm list`.

```bash
tvm install v13.2.2
tvm install v12.2.0
```

## Switching between tutor versions
To switch between tutor versions you should call

```bash
tvm use v<TUTOR_VERSION_INSTALLED>
```

## Installing a plugin in the current tutor version
To install a tutor plugin in the current tutor version you should call

```bash
tvm plugins install <PLUGIN_NAME/or/PLUGIN_LOCAL_PATH/or/PLUGIN_REPO>
```

## Listing tutor plugins
To list the tutor's plugins for each tutor version you should call

```bash
tvm plugins list
```

# Tutor enVironment Manager
tvm also is a tutor environment manager, which means that you can create one project and
set one version for it.

You will be able to continue using the tvm commands in your project.

- tvm list
- tvm plugins list
- tvm plugins install (this will install the plugins only in your project.)

## Creating a project
To create a new tvm project you should call
```bash
mkdir your-project && cd your-project
tvm project init
```
`--name`: to define a project name, if you don't define one, tvm will generate a random string.

`--version`: to define the tutor version, if you don't define one, tvm will use the current version.

This will create a tvm project and set **your-project** as **TUTOR_ROOT** and **TUTOR_PLUGINS_ROOT**

## Activating a project
To activate a project you should run

```bash
source .tvm/bin/activate
```

## Disabling a project
To disable a project you should run

```bash
tvmoff
```

**NOTE**: if you also enable another environment like python virtualenv, you need to deactivate each
virtual environment in order, that's mean:

```bash
# (venv) [v12.2.0@projectname] ->
deactivate
tvmoff

# [v12.2.0@projectname] (venv) ->
tvmoff
deactivate
```

**If you forgot to deactivate it in order, you will need to restart your shell terminal.**

# How to Contribute
Contributions are welcome!. See our [CONTRIBUTING](https://github.com/edunext/tvm/blob/master/CONTRIBUTING.md)
file for more information – it also contains guidelines for how to maintain high code quality, which will make your
contribution more likely to be accepted.

# License
The code in this repository is licensed under version 3 of the AGPL unless
otherwise noted. Please see the [LICENSE](https://github.com/edunext/tvm/blob/main/LICENSE) file for details.