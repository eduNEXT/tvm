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

## Setting tutor switcher
To set up a tutor switcher in your virtualenv you should call

```bash
tvm setup
```

If you want to set up it on /usr/local/bin/tutor (global) you should call
```bash
tvm setup -g
```

## Switching between tutor versions
To switch between tutor versions you should call

```bash
tvm use v<TUTOR_VERSION_INSTALLED>
```

## Installing a plugin in the current tutor version
To install a tutor plugin in the current tutor version you should call

```bash
tvm pip install <PLUGIN_NAME/or/PLUGIN_REPO>
```

## Listing tutor plugins
To list the tutor's plugins for each tutor version you should call

```bash
tvm plugins list
```

# How to Contribute
Contributions are welcome!. See our [CONTRIBUTING](https://github.com/edunext/tvm/blob/master/CONTRIBUTING.md)
file for more information – it also contains guidelines for how to maintain high code quality, which will make your
contribution more likely to be accepted.

# License
The code in this repository is licensed under version 3 of the AGPL unless
otherwise noted. Please see the [LICENSE](https://github.com/edunext/tvm/blob/main/LICENSE) file for details.