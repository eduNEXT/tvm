# What's TVM

TVM is the acronym for Tutor Version Manager. It manages Tutor versions and enables switching between them.

# Installing TVM

## GitHub

Open a terminal and run:

```bash
pip install git+https://github.com/eduNEXT/tvm.git@<TAG>
```

You can verify the installation with:

```bash
tvm --version
```

## Upgrading TVM (ToDo)

Currently, there isn't a command to do it, if you want to upgrade it, please install it again.

# Usage

## Quickstart

Create and activate a project with:

```bash
# Install a tutor version with
# tutor version mananger
tvm install v<tutor-version>

# Create a new project with
# tutor environment manager
tvm project <project-name> v<tutor-version>

# Move to the project
cd <project-name>

# Activate it
source .tvm/bin/activate
```

## Tutor Version Manager

A version manager for tutor, allows you to install and use different versions of tutor via the command line.

Access the complete guide of tutor version manager

- [Manage a tutor version](https://github.com/eduNEXT/tvm/blob/master/docs/TutorVersionManager.rst#manage-a-tutor-version)
- [Check tutor versions](https://github.com/eduNEXT/tvm/blob/master/docs/TutorVersionManager.rst#check-tutor-versions)
- [Switching between tutor versions](https://github.com/eduNEXT/tvm/blob/master/docs/TutorVersionManager.rst#switching-between-tutor-versions)
- [Configure tvm variables](https://github.com/eduNEXT/tvm/blob/master/docs/TutorVersionManager.rst#configure-tvm-variables)
- [Manage a plugin in the current tutor version](https://github.com/eduNEXT/tvm/blob/master/docs/TutorVersionManager.rst#manage-a-plugin-in-the-current-tutor-version)

## Tutor Environment Manager

Tutor environment manager allows you to create one project and set one version for it.

Access the complete guide of tutor version manager

- [Creating a project](https://github.com/eduNEXT/tvm/blob/master/docs/TutorEnvironmentManager.rst#creating-a-project)
- [Activate / Deactivate a project](https://github.com/eduNEXT/tvm/blob/master/docs/TutorEnvironmentManager.rst#activate--deactivate-a-project)
- [Check your projects](https://github.com/eduNEXT/tvm/blob/master/docs/TutorEnvironmentManager.rst#check-your-projects)
- [Manage a plugin in your project](https://github.com/eduNEXT/tvm/blob/master/docs/TutorEnvironmentManager.rst#manage-a-plugin-in-your-project)

# How to Contribute

Contributions are welcome!. See our [CONTRIBUTING](https://github.com/edunext/tvm/blob/master/CONTRIBUTING.md)
file for more information – it also contains guidelines for how to maintain high code quality, which will make your
contribution more likely to be accepted.

# License

The code in this repository is licensed under version 3 of the AGPL unless
otherwise noted. Please see the [LICENSE](https://github.com/edunext/tvm/blob/main/LICENSE) file for details.
